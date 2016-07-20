from django.shortcuts import render, get_object_or_404
from bio.guide import models


def guides(request):
    guides = models.Guide.objects.all()
    return render(request, 'bio/guides.html', {
        'meta': models.Guide._meta,
        'guides': guides
    })


def guide(request, guide_id):
    guide = get_object_or_404(models.Guide.objects.filter(id=guide_id))
    return render(request, 'bio/guide.html', {
        'guide': guide,
    })
