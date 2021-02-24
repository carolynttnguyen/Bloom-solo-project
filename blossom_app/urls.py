from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('login', views.login),
    path('register', views.register),
    path('create_user', views.create_user),
    path('bloomboard', views.show_bloomboard),
    path('checklist', views.show_checklist),
    # path('user_rules/<int:userId>', views.rules),
    path('journal_entry', views.journal_entry),
    path('delete_intention/<int:intentId>', views.delete_intention),
    path('delete_goal/<int:goalId>', views.delete_goal),
    path('delete-entry/<int:entryId>/<int:userId>', views.delete_entry),
    path('delete-quote/<int:quoteId>/<int:userId>', views.delete_quote),
    path('profile', views.profile),
    path('edit_profile/<int:userId>', views.edit_profile),
    path('edit_entry/<int:entryId>', views.edit_entry),
    path('edit_quote/<int:quoteId>', views.edit_quote),
    path('create_quote', views.create_quote),
    path('add_intention', views.add_intention),
    path('add_goal', views.add_goal),
    path('logout', views.logout)
]