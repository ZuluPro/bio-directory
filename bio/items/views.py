from django.shortcuts import render, get_object_or_404
from bio.items import models


def plantitems(request):
    plants = models.PlantItem.objects.order_by('type', 'seedling_date')
    return render(request, 'bio/plantitems.html', {
        'meta': plants.model._meta,
        'objects': plants
    })


def plantitem(request, plant_id):
    plant = get_object_or_404(models.PlantItem.objects.filter(id=plant_id))
    return render(request, 'bio/plantitem.html', {
        'plant': plant
    })
