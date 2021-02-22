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
    current_user = Users.objects.get(id=request.session['user_id'])

    # fetch user's friends data- all post 
    context = {
        'current_user': current_user,
    }
    return render(request, 'bloomboard.html', context)







def show_checklist(request):
    pass

def rules(request):
    pass

def journal_entry(request):
    pass

def create_quote(request):
    pass

def post_pic(request):
    pass

def logout(request):
    request.session.clear()
    return redirect('/')