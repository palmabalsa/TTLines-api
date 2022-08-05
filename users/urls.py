from django.urls import path
# from users.views import UserRegistration, LoginUser, AuthenticatedUser
from django.views.generic import TemplateView
from rest_framework import routers

app_name = 'users'

# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet, UserRegistration)

urlpatterns = [
    # path('all/', include (router.urls)),
    # path('', TemplateView.as_view(template_name="users/index.html")),
    # path('login/', LoginUser.as_view(), name="login"),
    # path('register/', UserRegistration.as_view(), name="registration"),
    # path('loggedin/', AuthenticatedUser.as_view(), name="authenticated"),
    
    # path('auth/', FireBaseAuthAPI.as_view(), name='firebase/auth'),
    # path('protected/', protected, name='protected'),
    # path('public/', public, name='public'),
]
