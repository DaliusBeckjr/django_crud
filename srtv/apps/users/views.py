from django.shortcuts import render, HttpResponse

from .models import User



def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")


def register(request):
    if request.method == "GET":
        return render(request, "register.html")

    if request.method == "POST":
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

        this_user = User.objects.create(first_name=request.POST['first_name'],
                                        last_name=request.POST['last_name'],
                                        email=request.POST['email'],
                                        password=pw_hash)
        return redirect('/')




def login(request):
    if request.method == "GET":
        return render(request, "login.html")

    if request.method == "POST":
        # this will search for the user inside the db
        this_user = User.objects.filter(email=request.POST['email'])
        
        # if the user exist
        if this_user:
            logged_user = this_user

            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['userid'] = logged_user.id
