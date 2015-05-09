from django.shortcuts import render
from models import *
from django.db.models import Q
# Create your views here.

def firstStep(request):

    materials = Material.objects.filter(type__in=['IQ','EN'])
    return render(request, 'firststep.html', {'materials':materials})
