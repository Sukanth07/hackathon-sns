from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('student/<str:username>/',views.student, name='student'),
    path('pillar_form/',views.pillar_form, name='pillar_form'),
    path('event_form_clt/',views.event_form_clt, name='event_form_clt'),
    path('event_form_scd/',views.event_form_scd, name='event_form_scd'),
    path('event_form_cfc/',views.event_form_cfc, name='event_form_cfc'),
    path('event_form_iipc/',views.event_form_iipc, name='event_form_iipc'),
    path('event_form_sri/',views.event_form_sri, name='event_form_sri'),
    path('view_activities/<str:username>/',views.view_activities, name='view_activities'),
]
