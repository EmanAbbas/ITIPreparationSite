from django.shortcuts import render
from models import *
# Create your views here.

def firstStep(request):

    materials = Material.objects.all()
    return render(request, 'firststep.html', {'materials':materials})
