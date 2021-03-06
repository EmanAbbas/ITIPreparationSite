from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import ReCaptchaField

from models import *



class QuestionForm(ModelForm):
    header = forms.CharField(label=_('Question'))
    type = forms.ChoiceField(label=_('Question Type'),choices=Question.type_choices)
    track_id = forms.ModelMultipleChoiceField(label=_('Choose Tracks'), queryset=Track.objects.all(), widget=forms.CheckboxSelectMultiple,required=False )
    image = forms.ImageField(label=_('Image'),required=False)
    class Meta:
        model = Question
        fields = ['header','type', 'track_id','image', 'user_id' ]


class AnswerForm(ModelForm):
    body = forms.CharField(widget=forms.Textarea(),label=_('body'))

    image = forms.ImageField(label=_('Image'), required=False)

    class Meta:
        model = Answer
        fields = ['question_id','body','image', 'user_id' ]



class MaterialForm(ModelForm):
    name = forms.CharField(label=_('Title'))
    description = forms.CharField(widget=forms.Textarea(),label=_('Description'),required=False)
    link = forms.URLField(label=_('Link'))
    type = forms.ChoiceField(label=_('Material Type'),choices=Material.type_choices)
    track_id = forms.ModelMultipleChoiceField(label=_('Choose Tracks'), queryset=Track.objects.all(), widget=forms.CheckboxSelectMultiple,required=False )

    class Meta:
        model = Material
        fields = ['name','description', 'link','type', 'track_id', 'user_id' ]


class registerationForm(UserCreationForm):
    captcha = ReCaptchaField(attrs={'theme' : 'clean'})