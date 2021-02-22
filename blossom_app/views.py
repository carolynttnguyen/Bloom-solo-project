from django.shortcuts import render, redirect
# from .models import *

# Create your views here.
def index(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def login (request):
    pass

def create_user(request):
    pass

def show_bloomboard(request):
    return render(request, 'bloomboard.html')

def show_checklist(request):
    pass

def rules(request):
    pass

def journal_entry(request):
    pass

def quote(request):
    pass

def flick(request):
    pass

def logout(request):
    request.session.clear()
    return redirect('/')