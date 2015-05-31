from django.shortcuts import render
from models import *
from django.http import JsonResponse
import json
from django.core import serializers
from django.db.models import Q

from django.views.generic import CreateView, FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
# Create your views here.

def firstStep(request,type):
    questions = Question.objects.filter(type=type)
    materials = Material.objects.filter(type=type)

    return render(request, 'firststep.html', {'materials':materials,'questions':questions})

def home(request):

    materials = Material.objects.filter(type__in=['IQ','EN'])
    return render(request, 'home.html', {'materials':materials,})


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


def Vote(request):

    result = dict()
    if not request.user.is_authenticated():
        result['status'] = 'NOT_LOGGED_IN'
    else:
        id = int(request.POST.get('id'))
        vote_type = request.POST.get('type')
        vote = int(request.POST.get('vote'))


        if vote_type == 'q':
            model = Question
        elif vote_type == 'a':
            model = Answer

        try:
            item = model.objects.get(pk=id)
        except:
            result['status'] = 'NOT_FOUND'
            return  JsonResponse(result)

        userVote = item.userVote(request.user)
        new_vote = userVote + vote

        if new_vote == 1:
            item.voteUpUsers.add(request.user)
        elif new_vote == -1:
            item.voteDownUsers.add(request.user)
        elif new_vote == 0:
            if userVote == 1:
                item.voteUpUsers.remove(request.user)
            elif userVote == -1:
                item.voteDownUsers.remove(request.user)

        result['votes'] = item.votes
        result['status'] = 'SUCCESS'
        # result['uservote'] = item.userVote(request.user)

    return  JsonResponse(result)

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy("home")


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = reverse_lazy("home")



