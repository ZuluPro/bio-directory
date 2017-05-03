import random

from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.views.generic import View, TemplateView
from django.views.generic.edit import FormView, UpdateView, CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy as reverse
from django.utils.translation import ugettext_lazy as _
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from askbot.conf import settings as askbot_settings

from bio import models as bio_models
from bio import forms as bio_forms
from . import models
from . import forms
from . import permissions
from . import utils


class HomeView(TemplateView):
    template_name = 'bio/contribute/home.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(HomeView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['last_questions'] = models.PlantQuestion.objects\
                                        .filter(validated=False)\
                                        .order_by('-date')[:5]
        context['last_validated_questions'] = models.PlantQuestion.objects\
                                                .filter(validated=True)\
                                                .order_by('-date')[:5]
        context['active_tab'] = 'wiki'
        return context


class ValidationHomeView(TemplateView):
    template_name = 'bio/contribute/validation_home.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ValidationHomeView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ValidationHomeView, self).get_context_data(**kwargs)
        context['last_plant_questions'] = models.PlantQuestion.objects\
                                            .order_by('-validated', '-date')[:5]
        context['last_new_plant'] = models.NewPlant.objects\
                                            .order_by('-validated', '-date')[:5]
        context['last_plant_images'] = models.PlantImage.objects\
                                            .order_by('-validated', '-date')[:5]
        return context


class ChoosePlantQuestionView(FormView):
    template_name = 'bio/contribute/choose_plant.html'
    form_class = forms.AddPlantQuestionForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ChoosePlantQuestionView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ChoosePlantQuestionView, self).get_context_data(**kwargs)
        context['plants'] = bio_models.Plant.objects.order_by('name')
        return context

    def form_valid(self, form):
        exists = bio_models.Plant.objects.filter(name=self.request.POST['name']).exists()
        if exists:
            self.instance = bio_models.Plant.objects.get(name=self.request.POST['name'])
            return super(ChoosePlantQuestionView, self).form_valid(form)

        submitted = models.NewPlant.objects.filter(name=self.request.POST['name']).exists()
        if submitted:
            new_plant = models.NewPlant.objects.filter(name=self.request.POST['name']).first()
            msg = _("%(plant_name)s has already been submitted. You can consult its <a href=\"%(new_plant_url)s\">file</a>.") % {
                'plant_name': new_plant.name,
                'new_plant_url': new_plant.get_absolute_url()
            }
            messages.info(self.request, msg)
            return redirect('contribute-plant')

        if permissions.user_can_add_plant(self.request.user):
            self.instance = bio_models.Plant.objects.create(name=self.request.POST['name'])
            msg = _("%(plant_name)s has been added to database. You can consult its <a href=\"%(plant_url)s\">file</a>.") % {
                'plant_name': self.instance.name,
                'plant_url': self.instance.get_absolute_url(),
            }
            messages.info(self.request, msg)
            return super(ChoosePlantQuestionView, self).form_valid(form)
        else:
            new_plant = models.NewPlant.objects.create(name=self.request.POST['name'],
                                                       user=self.request.user)
            msg = _("Your plant has been submitted. You can consult your submission <a href=\"%(new_plant_url)s\">here</a>") % {
                'new_plant_url': new_plant.get_absolute_url()
            }
            messages.info(self.request, msg)
            return redirect('contribute-plant')

    def get_success_url(self):
        return reverse('contribute-plant-home', args=(self.instance.id,))


class PlantView(DetailView):
    template_name = 'bio/contribute/plant.html'
    model = bio_models.Plant

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PlantView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PlantView, self).get_context_data(**kwargs)
        context['unknown_fields'] = [self.object._meta.get_field(f)
                for f in utils.get_plant_unknown_fields(self.object)][:5]
        random.shuffle(context['unknown_fields'])
        return context


class PlantQuestionView(FormView):
    template_name = 'bio/contribute/plant_question.html'
    model = bio_models.Plant
    form_class = forms.PlantQuestionForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PlantQuestionView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        try:
            return super(PlantQuestionView, self).get(request, *args, **kwargs)
        except utils.NoQuestionError as err:
            messages.info(self.request, _("All data about %(plant)s has been filled!") % {'plant': self.plant.name})
            return redirect('contribute-plant-home', self.plant.id)

    def post(self, request, *args, **kwargs):
        return super(PlantQuestionView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return forms.plant_question_form_factory(self.plant, self.fieldname, self.request.user)

    @property
    def fieldname(self):
        if not hasattr(self, '_fieldname'):
            self._fieldname = self.request.GET.get('fieldname') if self.request.method == 'GET' else self.request.POST.get('fieldname')
            if not self._fieldname:
                self._fieldname = utils.get_plant_unknown_field(self.plant, self.request.user)
        return self._fieldname

    @property
    def fields(self):
        return (self.fieldname, 'description')

    @property
    def plant(self):
        return self.model.objects.get(id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(PlantQuestionView, self).get_context_data(**kwargs)
        exclude = self.request.GET.getlist('exclude') if self.request.method == 'GET' else self.request.POST.getlist('exclude')
        form = self.get_form()
        form.instance = self.plant
        question = models.PlantQuestion(plant=self.plant, fieldname=self.fieldname)
        context.update({
            'fieldname': self.fieldname,
            'plant': self.plant,
            'exclude': exclude,
            'question': question
        })
        return context

    def form_invalid(self, form):
        import ipdb; ipdb.set_trace()

    def form_valid(self, form):
        if 'skip' in form.data:
            pass
        elif 'submit' in form.data:
            question = models.PlantQuestion(plant=self.plant,
                                            fieldname=self.fieldname,
                                            response=form.data.get(self.fieldname),
                                            reference=form.data.get('reference', ''),
                                            user=self.request.user)
            question.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('contribute-plant-question', args=(self.plant.id,))


class AddPlantImageFormView(CreateView):
    template_name = 'bio/contribute/plant_add_image.html'
    model = models.PlantImage
    form_class = forms.PlantImageForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AddPlantImageFormView, self).dispatch(*args, **kwargs)

    @property
    def plant(self):
        return bio_models.Plant.objects.get(id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(AddPlantImageFormView, self).get_context_data(**kwargs)
        context.update({
            'plant': self.plant
        })
        return context

    def get_success_url(self):
        msg = _("Your image has been submitted. Check it <a href=\"%(plant_image_url)s\">here</a>") % {
            'plant_image_url': self.object.get_absolute_url()
        }
        messages.info(self.request, msg)
        return reverse('contribute-plant-add-image', args=(self.plant.id,))


class ValidatePlantQuestionListView(ListView):
    template_name = 'bio/contribute/plant_validation_list.html'
    model = models.PlantQuestion
    paginate_by = 50

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ValidatePlantQuestionListView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        qs = self.model.objects.order_by('-date')
        if self.request.GET.get('hide_accepted') == 'yes':
            qs = qs.filter(validated=False)
        return qs

    def get_context_data(self, **kwargs):
        context = super(ValidatePlantQuestionListView, self).get_context_data(**kwargs)
        context.update({
          'hide_accepted': self.request.GET.get('hide_accepted') == 'yes'
        })
        return context


class ValidatePlantQuestionAutoPickView(View):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        question = utils.get_plant_validation_question(request.user)
        if question is None:
            messages.info(request, _("There's no data to validate"))
            return redirect('contribute-plant-question-validate-list')
        return redirect(question.get_absolute_url())


class ValidatePlantQuestionView(UpdateView):
    template_name = 'bio/contribute/plant_validation.html'
    model = models.PlantQuestion
    fields = ()

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ValidatePlantQuestionView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ValidatePlantQuestionView, self).get_context_data(**kwargs)
        context.update({
            'question': self.object,
            'has_voted': self.object.has_voted(self.request.user),
            'current_vote': self.object.get_user_vote_score(self.request.user),
        })
        if self.object.user == self.request.user:
            context.update({
              'disabled': True,
              'disabled_reason': _("You can't vote to your own question")
            })
        return context

    def form_valid(self, form):
        if 'skip' in form.data:
            pass
        elif 'validate' in form.data:
            if permissions.user_can_vote(self.request.user):
                self.object.vote_plus(self.request.user)
            else:
                messages.error(self.request, _("You can't vote"))
        elif 'decline' in form.data:
            if permissions.user_can_vote(self.request.user):
                self.object.vote_minus(self.request.user)
            else:
                messages.error(self.request, _("You can't vote"))
        elif 'neutral' in form.data:
            self.object.unvote(self.request.user)
        elif 'accept' in form.data and self.request.user.is_staff:
            if permissions.user_can_validate(self.request.user):
                messages.success(self.request, _("This response has been validated"))
                self.object.accept_response(self.request.user)
            else:
                messages.error(self.request, _("You can't decide answer validation"))
        elif 'unaccept' in form.data and self.request.user.is_staff:
            if permissions.user_can_validate(self.request.user):
                messages.success(self.request, _("This response has been unaccepted"))
                self.object.unaccept_response(self.request.user)
            else:
                messages.error(self.request, _("You can't decide answer validation"))
        return super(ValidatePlantQuestionView, self).form_valid(form)

    def get_success_url(self):
        return reverse('contribute-plant-question-validate-auto-pick')


class ValidateNewPlantQuestionAutoPickView(View):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        question = utils.get_new_plant_validation_question(request.user)
        if question is None:
            messages.info(request, _("There's no new plant to validate"))
            return redirect('contribute-new-plant-question-validate-list')
        return redirect(question.get_absolute_url())


class ValidateNewPlantQuestionListView(ListView):
    template_name = 'bio/contribute/new_plant_validation_list.html'
    model = models.NewPlant

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ValidateNewPlantQuestionListView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return self.model.objects.order_by('-date')


class ValidateNewPlantView(UpdateView):
    template_name = 'bio/contribute/new_plant_validation.html'
    model = models.NewPlant
    fields = ()

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ValidateNewPlantView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ValidateNewPlantView, self).get_context_data(**kwargs)
        context.update({
            'question': self.object,
            'has_voted': self.object.has_voted(self.request.user),
            'current_vote': self.object.get_user_vote_score(self.request.user),
        })
        if self.object.user == self.request.user:
            context.update({
              'disabled': True,
              'disabled_reason': _("You can't vote to your own question")
            })
        return context

    def form_valid(self, form):
        if 'skip' in form.data:
            pass
        elif 'validate' in form.data:
            if permissions.user_can_vote(self.request.user):
                self.object.vote_plus(self.request.user)
            else:
                messages.error(self.request, _("You can't vote"))
        elif 'decline' in form.data:
            if permissions.user_can_vote(self.request.user):
                self.object.vote_minus(self.request.user)
            else:
                messages.error(self.request, _("You can't vote"))
        elif 'neutral' in form.data:
            self.object.unvote(self.request.user)
        elif 'accept' in form.data:
            if permissions.user_can_validate(self.request.user):
                messages.success(self.request, _("%(plant)s has been added to database.") % {
                    'plant': self.object.name
                })
                self.object.accept_response(self.request.user)
            else:
                messages.error(self.request, _("You can't decide answer validation"))
        elif 'unaccept' in form.data:
            if permissions.user_can_validate(self.request.user):
                messages.success(self.request, _("This response has been unaccepted"))
                self.object.unaccept_response(self.request.user)
            else:
                messages.error(self.request, _("You can't decide answer validation"))
        return super(ValidateNewPlantView, self).form_valid(form)

    def get_success_url(self):
        return reverse('contribute-new-plant-question-validate-auto-pick')


class ValidateNewPlantImageAutoPickView(View):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        question = utils.get_plant_image_validation_question(request.user)
        if question is None:
            messages.info(request, _("There's no image to validate"))
            return redirect('contribute-plant-image-validate-list')
        return redirect(question.get_absolute_url())


class ValidatePlantImageListView(ListView):
    template_name = 'bio/contribute/plant_image_validation_list.html'
    model = models.PlantImage

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ValidatePlantImageListView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return self.model.objects.order_by('-date')


class ValidatePlantImageView(UpdateView):
    template_name = 'bio/contribute/plant_image_validation.html'
    model = models.PlantImage
    fields = ()

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ValidatePlantImageView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ValidatePlantImageView, self).get_context_data(**kwargs)
        context.update({
            'question': self.object,
            'has_voted': self.object.has_voted(self.request.user),
            'current_vote': self.object.get_user_vote_score(self.request.user),
        })
        if self.object.user == self.request.user:
            context.update({
              'disabled': True,
              'disabled_reason': _("You can't vote to your own question")
            })
        return context

    def form_valid(self, form):
        if 'skip' in form.data:
            pass
        elif 'validate' in form.data:
            if permissions.user_can_vote(self.request.user):
                self.object.vote_plus(self.request.user)
            else:
                messages.error(self.request.user, _("You can't vote"))
        elif 'decline' in form.data:
            if permissions.user_can_vote(self.request.user):
                self.object.vote_minus(self.request.user)
            else:
                messages.error(self.request, _("You can't vote"))
        elif 'neutral' in form.data:
            self.object.unvote(self.request.user)
        elif 'accept' in form.data:
            if permissions.user_can_validate(self.request.user):
                self.object.accept_response(self.request.user)
                messages.success(self.request, _("\"%(image_title)s\" has been added to database.") % {
                    'image_title': self.object.title
                })
                self.object.accept_response(self.request.user)
            else:
                messages.error(self.request, _("You can't decide answer validation"))
        elif 'unaccept' in form.data:
            if permissions.user_can_validate(self.request.user):
                self.object.unaccept_response(self.request.user)
            else:
                messages.error(self.request, _("You can't decide answer validation"))
        return super(ValidatePlantImageView, self).form_valid(form)

    def get_success_url(self):
        return reverse('contribute-plant-image-validate-auto-pick')
