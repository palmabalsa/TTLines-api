from django.urls import path
from firebase_auth.views import FireBaseAuthRegister

app_name = 'firebase_auth' 

  
   
   
urlpatterns = [
    path('auth/', FireBaseAuthRegister.as_view(), name='firebase/auth')
    # path('protected/', protected, name='protected'),
    # path('public/', public, name='public'),
]

