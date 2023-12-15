from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login 

from .models import User

import bcrypt # import it to the routes

def index(request):
    return render(request, "test.html", context)

def display(request, user_id):
    context = {
        'user' : User.objects.get(id = user_id)
    }
    return render(request, "test.html", context)



def register(request):
    if request.method == "GET":
        return render(request, "register.html")

    if request.method == "POST":
        errors = User.objects.user_validator(request.POST)
        if len(errors) > 0:
            for value in errors.values():
                messages.error(request, value)
            return redirect('/register')
        else:


            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

            this_user = User.objects.create(first_name=request.POST['first_name'],
                                            last_name=request.POST['last_name'],
                                            email=request.POST['email'],
                                            password=pw_hash)
            print(this_user.id)
            print(this_user.first_name)
            print(this_user.last_name)
            print(this_user.email)
            print(this_user.password)
            return redirect('/')




def login(request):
    if request.method == "GET":
        return render(request, "login.html")

    if request.method == "POST":
        errors = User.additional_objects.login_validator(request.POST)
        if len(errors) > 0: 

            for key, value in errors.items():
                messages.error(request, value)
                return redirect('/login')
        else:

        
            user = User.objects.filter(email=request.POST['email']).first()
            
            if user:
                logged_user = user
                
                if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                    request.session['userid'] = logged_user.id
                    return redirect('/')
# to protect routes --> if 'userid' not in request.session: return redirect('/')

# if 'email' not in postData['email'] or 'password' not in postData['password']:
#     messages.errors ="email and password fields are required"
