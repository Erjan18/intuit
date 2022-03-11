from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('header/',HeadisView.as_view,name='header'),
    path('head/',HeadView.as_view(),name='head'),
    path('headdis/',HeaderView.as_view(),name='headdis'),
    path('career/',CareerView.as_view(),name='career'),
    path("feedback/",FeedBackView.as_view(),name='feedback'),
    path('r/<str:topic>/', RandomQuestion.as_view(), name='random'),
    path('q/<str:topic>/', QuizQuestion.as_view(), name='questions'),
    path('job/',Job_fairView.as_view(),name='job'),
    path('reception/',Reception_campaignView.as_view(),name='reception'),
    path('form/',Forms_of_trainingView.as_view(),name='form'),
    path('description/',Description_formView.as_view(),name='description'),
    path('open/',Open_dayView.as_view(),name='open'),
    path('news/',News_blogView.as_view(),name='news'),
    path('connect/',ConnectView.as_view(),name='connect'),
    path('upload/',FileView.as_view(),name='upload'),
    path('abi/',AbiturientView.as_view(),name='abi'),
    path('center/',CenterView.as_view(),name='center'),
    path('student/',StudentView.as_view(),name='student'),
    path('enactus/',EnactusView.as_view(),name='enactus'),
    path('about/',AboutView.as_view(),name='about')

]
