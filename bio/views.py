from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.shortcuts import render, get_object_or_404

from bio import models


class HomeView(TemplateView):
    template_name = 'bio/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context


def directories(request):
    return render(request, 'bio/directories.html', {})


class PlantListView(ListView):
    model = models.Plant
    template_name = 'bio/plant_list.html'

    def get_queryset(self):
        qs = self.model.objects.order_by('name')
        if self.request.GET.get('q'):
            qs = qs.filter(name__icontains=self.request.GET['q'])
        return qs

    def get_context_data(self, **kwargs):
        context = super(PlantListView, self).get_context_data(**kwargs)
        context['meta'] = self.model._meta
        return context


def plants(request):
    plants = models.Plant.objects\
                .order_by('name')
    if request.GET.get('q'):
        plants = plants.filter(name__icontains=request.GET['q'])
    return render(request, 'bio/plant_list.html', {
        'meta': plants.model._meta,
        'objects': plants
    })


def plant(request, plant_id):
    plant = get_object_or_404(models.Plant.objects.filter(id=plant_id))
    return render(request, 'bio/plant.html', {
        'plant': plant
    })


def pathologies(request):
    pathologies = models.Pathology.objects.all()
    return render(request, 'bio/directory.html', {
        'meta': pathologies.model._meta,
        'objects': pathologies
    })


def pathology(request, pathology_id):
    pathology = get_object_or_404(models.Pathology.objects.filter(id=pathology_id))
    return render(request, 'bio/pathology.html', {
        'pathology': pathology
    })


def pests(request):
    pests = models.Pest.objects.all()
    return render(request, 'bio/directory.html', {
        'meta': pests.model._meta,
        'objects': pests
    })


def pest(request, pest_id):
    pest = get_object_or_404(models.Pest.objects.filter(id=pest_id))
    return render(request, 'bio/pest.html', {
        'pest': pest
    })
