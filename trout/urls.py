from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'trout'

urlpatterns = [
    # path('', views.index, name = 'index'),
    # path('catchdata/', views.catchdata, name= 'catchdata'),
    # class based views ====
    path('', TemplateView.as_view(template_name="trout/index.html")),
    path('catchdata/', TemplateView.as_view(template_name="trout/catchdata.html")),
    path('logout/', views.logout, name= 'logout'),
    
    
]