from django.shortcuts import render

# Create your views here.

def firstStep(request):
    return render(request, 'firststep.html')
