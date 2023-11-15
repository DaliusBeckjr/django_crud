from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse

# Create your views here.
def index(request):
    # return HttpResponse('welcome to django')
    return redirect('shows/dashboard')