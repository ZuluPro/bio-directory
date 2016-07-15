from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now
from schedule.models import Calendar
from schedule.periods import Day
from bio.scheduler import models


def actions(request):
    actions = models.Action.objects.order_by('-created_on')
    period = Day(actions, now())
    # XXX: Hack for don't get tomorow occs
    occs = [occ for occ in period.get_occurrences()
            if occ.start.date() == now().date()]
    return render(request, 'bio/actions.html', {
        'meta': actions.model._meta,
        'objects': occs,
        'calendar': Calendar.objects.get(name='Bio')
    })


def action(request, action_id):
    action = get_object_or_404(models.Action.objects.filter(id=action_id))
    return render(request, 'bio/action.html', {
        'action': action
    })
