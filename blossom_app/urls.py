from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('login', views.login),
    path('register', views.register),
    path('create_user', views.create_user),
    path('bloomboard', views.show_bloomboard),
    path('checklist', views.show_checklist),
    path('user_rules/<int:userId>', views.rules),
    path('journal_entry', views.journal_entry),
    path('delete_intention/<int:intentId>', views.delete_intention),
    path('delete_goal/<int:goalId>', views.delete_goal),
    path('profile/<int:userId>', views.profile),
    path('edit_profile', views.edit_profile),
    path('create_quote', views.create_quote),
    path('add_intention', views.add_intention),
    path('add_goal', views.add_goal),
    path('logout', views.logout)
]