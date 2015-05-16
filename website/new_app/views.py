from django.shortcuts import render
from models import *
from django.db.models import Q
# Create your views here.

def firstStep(request):

    materials = Material.objects.filter(type__in=['IQ','EN'])
    return render(request, 'firststep.html', {'materials':materials})


def tracks(request):
    all_tracks = Track.objects.all()

    return render(request,'tracks.html',{'tracks':all_tracks, 'track':all_tracks[0]})

def track_details(request, track_id):

    track = Track.objects.get(pk=track_id)
    all_tracks = Track.objects.all()

    return render(request,'tracks.html',{'tracks':all_tracks, 'track':track})