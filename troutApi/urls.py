from django.urls import path
from .views import EditOrDeleteLogEntry, FishList, CreateLogEntry, ListUsers, TrialEndPointFishList

app_name = 'troutApi'

urlpatterns = [
    path('all/', TrialEndPointFishList.as_view(), name = 'trialEndPoint'),
    path('listallusers/', ListUsers.as_view(), name = 'listusers'),
    path('log/', FishList.as_view(), name = 'fishingloglist'),
    path('create/', CreateLogEntry.as_view(), name = 'create'),
    path('log/<int:id>', EditOrDeleteLogEntry.as_view(), name= 'updatedelete'),
]