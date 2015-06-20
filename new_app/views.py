from django.shortcuts import render, redirect,get_object_or_404
from models import *
from forms import *
from django.http import JsonResponse
import json
from django.core import serializers
from django.db.models import Q

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.views.generic import CreateView, FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core.urlresolvers import reverse_lazy

from django.utils.translation import ugettext_lazy as _

from copy import deepcopy

from haystack.query import SearchQuerySet
# Create your views here.

def firstStep(request,type):
    questions = Question.objects.filter(type=type, status=Question.status_choices[1][0])
    materials = Material.objects.filter(type=type)


    # questions_paginator = Paginator(questions,2)
    #
    # page = request.GET.get("page")
    # try:
    #     questions = questions_paginator.page(page)
    # except PageNotAnInteger:
    #     questions = questions_paginator.page(1)
    # except EmptyPage:
    #     questions = questions_paginator.page(questions_paginator.num_pages)

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
    questions = track.question_set.filter(status=Question.status_choices[1][0])

    context['track'] = track
    context['materials'] = materials
    context['questions'] = questions

    return render(request,'tracks.html',context)


def FAQ(request):
    FAQs = Question.objects.filter(type='FAQ', status=Question.status_choices[1][0])

    return render(request,'faqs.html',{'questions':FAQs})

@login_required
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
        elif vote_type == 'm':
            model = Material

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


def search_questions(request):
    if request.POST:
        questions = SearchQuerySet().autocomplete(content_auto = request.POST.get('search_text',''))
    else:
        questions = None
    return render(request,'search.html',{'questions':questions, 'post':request.POST})

@login_required
def add_question(request):
    msg = None

    form = QuestionForm()

    if request.method == 'POST':
        data = deepcopy(request.POST)
        data['user_id'] = request.user.id
        form = QuestionForm(data=data, files=request.FILES)

        if form.is_valid():
            form.save()
            form = QuestionForm()
            msg=_('Question Added Successfully')


    del form.fields['user_id']
    return render(request,'addquestion.html',{'form':form,'msg':msg})


def question_details(request,id):
    context = {}

    q = get_object_or_404(Question,pk=id)

    form = AnswerForm()
    msg = None
    
    if request.method == 'POST':
        if request.user.is_authenticated:
            data = deepcopy(request.POST)
            data['user_id'] = request.user.id
            data['question_id'] = id
            form = AnswerForm(data=data, files=request.FILES)

            if form.is_valid():
                form.save()
                form = AnswerForm()
                msg=_('Answer sent Successfully')
        else:
            msg=_('Your aren\'t authenticated')



    del form.fields['user_id']
    del form.fields['question_id']

    context['question'] = q
    context['form'] = form
    context['msg'] = msg


    return render(request,'question-details.html',context)

@staff_member_required
def moderate(request):
    context = {}

    new_questions = Question.objects.filter(status=Question.status_choices[0][0])
    new_answers = Answer.objects.filter(status=Answer.status_choices[0][0])

    context['new_questions'] = new_questions.count()
    context['new_answers'] = new_answers.count()

    return render(request,'moderate/home.html',context)

@staff_member_required
def moderate_new_questions(request):
    context = {}

    new_questions = Question.objects.filter(status=Question.status_choices[0][0])


    context['new_questions'] = new_questions


    return render(request,'moderate/newquestions.html',context)



@staff_member_required
def moderate_new_answers(request):
    context = {}

    new_answers = Answer.objects.filter(status=Answer.status_choices[0][0])


    context['new_answers'] = new_answers


    return render(request,'moderate/newanswers.html',context)




@staff_member_required
def approve_question(request):

    result = dict()
    if not request.user.is_staff:
        result['status'] = 'NOT_STAFF'
    else:
        id = int(request.POST.get('id'))
        try:
            q = Question.objects.get(pk=id)
            q.status = Question.status_choices[1][0]
            q.save()
            result['status'] = 'SUCCESS'
        except:
            result['status'] = 'NOT_FOUND'

    return  JsonResponse(result)


@staff_member_required
def reject_question(request):

    result = dict()
    if not request.user.is_staff:
        result['status'] = 'NOT_STAFF'
    else:
        id = int(request.POST.get('id'))
        try:
            q = Question.objects.get(pk=id)
            q.status = Question.status_choices[2][0]
            q.save()
            result['status'] = 'SUCCESS'
        except:
            result['status'] = 'NOT_FOUND'

    return  JsonResponse(result)




@staff_member_required
def approve_answer(request):

    result = dict()
    if not request.user.is_staff:
        result['status'] = 'NOT_STAFF'
    else:
        id = int(request.POST.get('id'))
        try:
            a = Answer.objects.get(pk=id)
            a.status = Answer.status_choices[1][0]
            a.save()
            result['status'] = 'SUCCESS'
        except:
            result['status'] = 'NOT_FOUND'

    return  JsonResponse(result)


@staff_member_required
def reject_answer(request):

    result = dict()
    if not request.user.is_staff:
        result['status'] = 'NOT_STAFF'
    else:
        id = int(request.POST.get('id'))
        try:
            a = Answer.objects.get(pk=id)
            a.status = Answer.status_choices[2][0]
            a.save()
            result['status'] = 'SUCCESS'
        except:
            result['status'] = 'NOT_FOUND'

    return  JsonResponse(result)





class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy("home")


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = reverse_lazy("home")






