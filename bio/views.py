from django.shortcuts import render, get_object_or_404
from bio import models


def directories(request):
    return render(request, 'bio/directories.html', {})


def plants(request):
    plants = models.Plant.objects.all()
    return render(request, 'bio/directory.html', {
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
