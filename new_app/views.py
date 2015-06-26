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
from django.contrib.auth import authenticate, login

from django.utils.translation import ugettext_lazy as _

from copy import deepcopy

from haystack.query import SearchQuerySet
# Create your views here.




def materials(request,type,track_id):

    track = None
    material = Material.objects.filter(type=type, status=Material.status_choices[1][0])

    if track_id:
        material = material.filter(track_id=track_id)
        track = get_object_or_404(Track,pk=track_id)

    material = sorted(material, key=lambda x: -x.votes)
    paginator = Paginator(material,10)

    page = request.GET.get("page")
    try:
        material = paginator.page(page)
    except PageNotAnInteger:
        material = paginator.page(1)
    except EmptyPage:
        material = paginator.page(paginator.num_pages)



    context = {}
    context['materials'] = material
    context['track'] = track
    context['type'] = type
    return render(request, 'materials.html',context)


def questions(request,type,track_id):
    track = None
    question = Question.objects.filter(type=type, status=Material.status_choices[1][0])

    if track_id:
        question = question.filter(track_id=track_id)
        track = get_object_or_404(Track,pk=track_id)

    question = sorted(question, key=lambda x: -x.votes)
    paginator = Paginator(question,10)

    page = request.GET.get("page")
    try:
        question = paginator.page(page)
    except PageNotAnInteger:
        question = paginator.page(1)
    except EmptyPage:
        question = paginator.page(paginator.num_pages)



    context = {}
    context['questions'] = question
    context['track'] = track
    context['type'] = type
    return render(request, 'questions.html',context)



def home(request):

    materials = Material.objects.filter(type__in=['IQ','EN'])
    return render(request, 'home.html', {'materials':materials,})


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


@login_required
def add_material(request):
    msg = None

    form = MaterialForm()

    if request.method == 'POST':
        data = deepcopy(request.POST)
        data['user_id'] = request.user.id
        form = MaterialForm(data=data)

        if form.is_valid():
            form.save()
            form = MaterialForm()
            msg=_('Material Added Successfully')


    del form.fields['user_id']
    return render(request,'addmaterial.html',{'form':form,'msg':msg})


@staff_member_required
def moderate(request):
    context = {}

    new_questions = Question.objects.filter(status=Question.status_choices[0][0])
    new_answers = Answer.objects.filter(status=Answer.status_choices[0][0])
    new_materials = Material.objects.filter(status=Answer.status_choices[0][0])

    context['new_questions'] = new_questions.count()
    context['new_answers'] = new_answers.count()
    context['new_materials'] = new_materials.count()

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
def moderate_new_materials(request):
    context = {}

    new_materials = Material.objects.filter(status=Material.status_choices[0][0])


    context['new_materials'] = new_materials


    return render(request,'moderate/newmaterials.html',context)



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




@staff_member_required
def approve_material(request):

    result = dict()
    if not request.user.is_staff:
        result['status'] = 'NOT_STAFF'
    else:
        id = int(request.POST.get('id'))
        try:
            m = Material.objects.get(pk=id)
            m.status = Material.status_choices[1][0]
            m.save()
            result['status'] = 'SUCCESS'
        except:
            result['status'] = 'NOT_FOUND'

    return  JsonResponse(result)


@staff_member_required
def reject_material(request):

    result = dict()
    if not request.user.is_staff:
        result['status'] = 'NOT_STAFF'
    else:
        id = int(request.POST.get('id'))
        try:
            m = Material.objects.get(pk=id)
            m.status = Material.status_choices[2][0]
            m.save()
            result['status'] = 'SUCCESS'
        except:
            result['status'] = 'NOT_FOUND'

    return  JsonResponse(result)




def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.backend='django.contrib.auth.backends.ModelBackend'
            login(request,new_user)
            return redirect('home')

    return render(request,'signup.html',{'form':form})

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy("home")


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = reverse_lazy("home")






