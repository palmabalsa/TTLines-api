from django.urls import path, include
# from users.views import UserList, UserDetail
from django.views.generic import TemplateView
# from rest_framework import routers
from users.views import AuthenticatedView, HelloView, RegisterUser

app_name = 'users'

# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
    path('verified', AuthenticatedView.as_view()),
    path('register', RegisterUser.as_view()),
    path('hello', HelloView.as_view()),
    
    
    
    
    
    
    
    
    
    
    
    
    
    # path('', include (router.urls)),
    # path('fisherman/', UserList.as_view()),
    # path('fisherman/<int:pk>', UserDetail.as_view()),
    
    # path('', TemplateView.as_view(template_name="users/index.html")),
    # path('login/', LoginUser.as_view(), name="login"),
    # path('register/', UserRegistration.as_view(), name="registration"),
    # path('loggedin/', AuthenticatedUser.as_view(), name="authenticated"),
    
    # path('auth/', FireBaseAuthAPI.as_view(), name='firebase/auth'),
    # path('protected/', protected, name='protected'),
    # path('public/', public, name='public'),
]
