from django.shortcuts import render
from rest_framework import generics
from trout.models import CatchData
from troutApi.serializers import CatchDataSerializer, NewFishSerializer, SuperBasicSerializer
from rest_framework.permissions import IsAuthenticated


# these generic views contain all the 'CRUD' type stuff behind the scenes
class FishList(generics.ListAPIView): #lists all your catches
    # permission_classes = [IsAuthenticated]
    queryset = CatchData.objects.all()
    serializer_class = NewFishSerializer


class LogNewCatch(generics.CreateAPIView): #lets you log new catch
    # permission_classes = [IsAuthenticated]
    queryset = CatchData.objects.all()
    # serializer_class = SuperBasicSerializer
    serializer_class = NewFishSerializer
  
    
    
class UpdateOrDeleteCatch(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = CatchData.objects.all()
    serializer_class = CatchDataSerializer
    
    
class DeleteCatch(generics.DestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = CatchData.objects.all()
    serializer_class = CatchDataSerializer
    
    
class PostDetail(generics.ListAPIView):
    queryset = SuperBasicSerializer
    pass
    # permission_classes = [IsAuthenticated]


    
  