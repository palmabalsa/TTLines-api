from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required




# Create your views here.

# dont need these 2 anymore as used class-based views (template view)
# def index(request):
#     return render(request, 'trout/index.html')

# def catchdata(request):
#     return render(request, 'trout/catchData.html')

@login_required
def logout(request):
    django_logout(request)
    domain = settings.SOCIAL_AUTH_AUTH0_DOMAIN
    client_id = settings.SOCIAL_AUTH_AUTH0_KEY
    return_to = 'http://127.0.0.1:8000/'
    return redirect (f'https://{domain}/v2/logout?client_id={client_id}&returnTo={return_to}')

