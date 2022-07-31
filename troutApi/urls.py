from django.urls import path
from .views import DeleteCatch, FishList, LogNewCatch, UpdateOrDeleteCatch


app_name = 'troutApi'


# these are our 2 api-endpoints ::::
# need to create a view for each

urlpatterns = [
    # this one takes in a primary key (pk) and is called detailcreate
    # this view shows an single component/object in the database
    path('<int:pk>/', UpdateOrDeleteCatch.as_view(), name = 'updatedelete'),
    # # here you create a new catch
    path('create/', LogNewCatch.as_view(), name = 'create'),
    # # this one takes no input, and is the homepage, called 'listcreate'
    # # this view shows all the data in our database
    # lists all the data in our database
    path('', FishList.as_view(), name = 'list'),
    path('<int:pk>/delete', DeleteCatch.as_view(), name = 'delete'),
]