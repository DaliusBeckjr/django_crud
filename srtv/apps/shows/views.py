from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse

from django.contrib import messages

from .models import Show, User

# Create your views here.
def index(request):
    return redirect('dashboard') # interesting...

def dashboard(request):
    # all_shows = Show.objects.all()
    # for show in all_shows:
    #     print(show)
    
    # more of a common way to pass information
    context = {
        'all_shows' : Show.objects.all()
    }
    return render(request, 'index.html', context)

def add_show(request):
    if request.method == 'GET': # not really a big need but i like to specify
        return render(request, 'create.html')
    if request.method == 'POST':
        errors = Show.objects.show_validate(request.POST)
        if len(errors) > 0:
            
            # for key, value in errors.items(): # .items() is a tuple for the key but if we
            for value in errors.values():
                messages.error(request, value)
            return redirect(f'/shows/new')
        else:
        # another form of session like flask
            print('Got POST info..........')
            # print(request.POST)
            # print(request.POST['title']) # to get a single key value we can do
            this_show = Show.objects.create(title=request.POST['title'],
                                network=request.POST['network'],
                                released_on=request.POST['released_on'],
                                description=request.POST['description'],
                                creator= User.objects.get(id = 1))
            print(this_show.id) # views the new show id
            print(this_show.title) # views the new show id
            print(this_show.network) # views the new show id
            print(this_show.released_on) # views the new show id
            print(this_show.description) # views the new show id
            return redirect(f'/shows/{this_show.id}') # interesting compared to the other routes

def display(request, show_id):
    
    context = {
        'show' : Show.objects.get(id = show_id)
    }
    return render(request, 'display.html', context)

def update(request, show_id):
    this_show =  Show.objects.get(id = show_id)

    if request.method == 'POST':
        this_show.title = request.POST['title']
        this_show.network = request.POST['network']
        this_show.released_on = request.POST['released_on']
        this_show.description = request.POST['description']
        this_show.creator = User.objects.get(id = 1)
        this_show.save()
        return redirect(f'/shows/{show_id}')

    context = {
        'show' : this_show
    }
    return render(request, 'edit.html', context)

def delete(request, show_id):
    # Show.objects.get(id = show_id).delete() # one way 
    delete_show = Show.objects.get(id = show_id)
    delete_show.delete()
    return redirect('/')
