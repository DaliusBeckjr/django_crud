from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from .models import User

import bcrypt # import it to the routes

def index(request):
    return HttpResponse("whats good")


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
        errors = User.objects.user_validator(request.POST)
        if len(errors) > 0:
            for value in errors.values():
                messages.error(request, value)
            return redirect('/login')
        else:
        # this will search for the user inside the db
        # usually we use filter for a queryset but can use it without
        # added a .first() to retrieve the first user if it exist
            this_user = User.objects.filter(email=request.POST['email']).first()
            
            # if the user exist
            if this_user:
                logged_user = this_user

                if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                    request.session['userid'] = logged_user.id
                    print("this is the guy")
                    return redirect('/')
    print("invalid password")
    return redirect('/login')
# to protect routes --> if 'userid' not in request.session: return redirect('/')
