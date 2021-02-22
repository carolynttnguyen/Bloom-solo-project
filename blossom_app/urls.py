from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('login', views.login),
    path('register', views.register),
    path('create_user', views.create_user),
    path('bloomboard', views.show_bloomboard),
    path('checklist', views.show_checklist),
    path('user_rules', views.rules),
    path('journal_entry', views.journal_entry),
    path('quote', views.quote),
    path('flick', views.flick),
    path('logout', views.logout)
]