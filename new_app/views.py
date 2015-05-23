from django.shortcuts import render
from models import *
from django.db.models import Q
# Create your views here.

def firstStep(request):

    materials = Material.objects.filter(type__in=['IQ','EN'])
    return render(request, 'firststep.html', {'materials':materials,})

def home(request):

    materials = Material.objects.filter(type__in=['IQ','EN'])
    return render(request, 'firststep.html', {'materials':materials,})


def tracks(request):
    all_tracks = Track.objects.all()

    return render(request,'tracks.html',{'track':all_tracks[0]})

def track_details(request, track_id):
    context = {}

    track = Track.objects.get(pk=track_id)

    materials = track.material_set.all()
    questions = track.question_set.all()

    context['track'] = track
    context['materials'] = materials
    context['questions'] = questions

    return render(request,'tracks.html',context)


def FAQ(request):
    FAQs = Question.objects.filter(type='FAQ')

    return render(request,'faqs.html',{'questions':FAQs})