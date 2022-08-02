from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required




# Create your views here.

# dont need these 2 anymore as used class-based views (template view)
# def index(request):
#     return render(request, 'trout/index.html')

# def fishinglog(request):
#     return render(request, 'trout/fishinglog.html')