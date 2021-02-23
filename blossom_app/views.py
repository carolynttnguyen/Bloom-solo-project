from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def index(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    if "user_id" in request.session:
        redirect('/bloomboard')
    if request.method=='POST':
        login_errors = Users.objects.LoginValidator(request.POST)
        # validate input
        if login_errors:
            for error in login_errors:
                messages.error(request, login_errors[error])
            return redirect('/')

        logged_user = Users.objects.filter(username=request.POST['log_username'])
        # check if user email is DB
        if logged_user:
            logged_user=logged_user[0]
            if bcrypt.checkpw(request.POST['log_password'].encode(), logged_user.password.encode()):
                request.session['user_id']= logged_user.id
                # logged_user = request.session['user_id'] 
                request.session['username']= logged_user.username
            return redirect('/bloomboard')
    return redirect('/')


def create_user(request):
    if request.method =='POST':
        errors = Users.objects.RegistrationValidator(request.POST)
        # validate input
        if errors:
            for error in errors:
                messages.error(request, errors[error])
            return redirect('/register')

        # check is user email already exist
        existing_user_list = Users.objects.filter(email=request.POST['email'])
        
        if len(existing_user_list) > 0 :
            messages.error(request, 'Email already exist. Try using another Email Address.')
            return redirect('/register')
        
        # Create user
        user_pw = request.POST['password']
        hash_pw = bcrypt.hashpw(user_pw.encode(), bcrypt.gensalt()).decode()
        print(hash_pw)

        new_user = Users.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            username = request.POST['username'],
            email = request.POST['email'],
            password = hash_pw,
            reasons = request.POST['reasons'],
            personal_quote = request.POST['personal_quote']
        )

        # set session data
        request.session['user_id']= new_user.id
        # current_user = request.session['user_id']
        request.session['username'] = new_user.username
        return redirect('/bloomboard')
    

def show_bloomboard(request):
    # fetch User's personal data - reason, quote, post
    # fetch user's friends data- all post 
    if request.method =="GET":
        current_user = Users.objects.get(id=request.session['user_id'])
        context = {
            'current_user': current_user,
            # 'current_user_entries': Journal_Entires.objects.filter(user=current_user),
            # 'current_user_quotes': Quotes.objects.filter(user=current_user),
            # 'user_friends': Friends.objects.filter(user=current_user),
            'entries': Journal_Entires.objects.all().order_by("-created_at"),
            # 'quotes': Quotes.objects.all().filter("-created_at")
            }
        return render(request, 'bloomboard.html', context)

def profile(request):
    if request.method=="GET":
        # users-quotes, journal entries, rules, regulators, reason
        context = {
            
        }
    return render(request, 'bloom_profile.html', context)

def edit_profile(request):
    if request.method =='GET':
        context = {}
        return render(request, 'edit_profile.html', context)
    else:
        # update & save changes rules, regulators, quote, reason, rules
        return redirect('/profile')

def show_checklist(request):
    if request.method =='GET':
        context = {
            'current_user':Users.objects.get(id=request.session['user_id']),
            'goals': Goals.objects.filter(user=request.session['user_id']),
            'intentions': Intentions.objects.filter(user= request.session['user_id'])
        }
    return render(request, 'checklist.html', context)

def rules(request, userId): 
    # grab other users id, ad redirects to their profile
    context = {}
    return render(request, 'profile.html, context')

def journal_entry(request):
    if request.method =='POST':
        new_intention = Journal_Entries.objects.create(
            entry = request.POST['entry'],
            user = Users.objects.get(id = request.session['user_id'])
        )
        return redirect('/bloomboard')
    return redirect('/bloomboard')

def create_quote(request):
    if request.method =='POST':
        new_intention = Quotes.objects.create(
            the_quote = request.POST['quote'],
            quote_author = request.POST['author'],
            user = Users.objects.get(id=request.session['user_id'])
        )
        return redirect('/bloomboard')
    return redirect('/bloomboard')

def delete_intention(request, intentId):
    to_be_deleted = Intentions.objects.get(id=intentId)
    to_be_deleted.delete()
    return redirect('/checklist')

def add_intention(request):
    if request.method =='POST':
        new_intention = Intentions.objects.create(
            intention = request.POST['intention'],
            user = Users.objects.get(id=request.session['user_id'])
        )
        
        return redirect('/checklist')
    return redirect('/checklist')

def add_goal(request):
    if request.method =='POST':
        new_intention = Goals.objects.create(
            goal = request.POST['goal'],
            user = Users.objects.get(id=request.session['user_id'])
        )
        return redirect('/checklist')
    return redirect('/checklist')

def delete_goal(request, goalId):
    delete_goal= Goals.objects.get(id=goalId)
    delete_goal.delete()
    return redirect('/checklist')

def logout(request):
    request.session.clear()
    return redirect('/')