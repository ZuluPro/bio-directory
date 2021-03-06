from django.shortcuts import render, get_object_or_404
from bio.items import models


def plantitems(request):
    plantsets = models.PlantSet.objects.filter(active=True)
    return render(request, 'bio/plantitems.html', {
        'meta': models.PlantItem._meta,
        'plantsets': plantsets
    })


def plantitem(request, plant_id):
    plant = get_object_or_404(models.PlantItem.objects.filter(id=plant_id))
    actions = plant.action_set.all() if hasattr(plant, 'action_set') else []
    return render(request, 'bio/plantitem.html', {
        'plant': plant,
        'actions': actions,
    })
