"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.conf import settings
from django.contrib import admin
from new_app.views import *


admin.autodiscover()
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^firststep/([A-Z]+)/$', firstStep, name='firststep'),
    url(r'^$', home, name='home'),
    # url(r'^tracks/$', tracks, name='tracks'),
    # url(r'^track/([0-9]+)/$', track_details, name='track'),

    url(r'^newquestion/$', add_question, name='add_question'),
    url(r'^question/details/(?P<id>[0-9]+)/$', question_details, name='question_details'),


    url(r'^moderate/$', moderate, name='moderate'),
    url(r'^moderate/newquestions$', moderate_new_questions, name='moderate_new_questions'),
    url(r'^moderate/newanswers$', moderate_new_answers, name='moderate_new_answers'),
    url(r'^moderate/newmaterials$', moderate_new_materials, name='moderate_new_materials'),


    # url(r'^faq/$', FAQ, name='FAQs'),

    url(r'^vote/$', Vote, name='vote'),


    url(r'^materials/(?P<type>[a-zA-Z]+)/(?P<track_id>[0-9]*)$', materials, name='materials'),
    url(r'^questions/(?P<type>[a-zA-Z]+)/(?P<track_id>[0-9]*)$', questions, name='questions'),



    url(r'^newmaterial/$', add_material, name='add_material'),


    url(r'^approve/question$', approve_question, name='approve_question'),
    url(r'^reject/question$', reject_question, name='reject_question'),



    url(r'^approve/answer$', approve_answer, name='approve_answer'),
    url(r'^reject/answer$', reject_answer, name='reject_answer'),

    url(r'^approve/material$', approve_material, name='approve_material'),
    url(r'^reject/material$', reject_material, name='reject_material'),

    # url(r'^signup/$', SignUpView.as_view(), name='signup'),
    url(r'^signup/$', register, name='signup'),

    url(r'^testsearch/$', search_questions),

    url(r'^search/$', include('haystack.urls')),


]

urlpatterns += patterns(
    'django.contrib.auth.views',

    url(r'^login/$', 'login',{'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', 'logout',{'next_page': 'home'}, name='logout'),


                        )


if settings.DEBUG :
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )


