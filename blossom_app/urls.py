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
    path('create_quote', views.create_quote),
    path('post_pic', views.post_pic),
    path('logout', views.logout)
]