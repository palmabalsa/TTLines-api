from rest_framework import generics
from firebase_auth.authentication import FirebaseBackend
from trout.models import FishingLogEntry
from troutApi.serializers import CatchDataSerializer, NewFishSerializer, SuperBasicSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from users.serializers import UserSerializer

# from firebase_admin import auth
from django.contrib.auth import get_user_model

User = get_user_model()

# test endpoint displaying all data without loggin in


class TrialEndPointFishList(generics.ListAPIView):
    authentication_classes = []
    # permission_classes = []
    permission_classes = ()
    serializer_class = NewFishSerializer
    print (serializer_class.data)
    queryset = FishingLogEntry.objects.all()
    

class FishList(generics.ListAPIView):
    # authentication_classes = [FirebaseBackend,]
    # permission_classes = [IsAuthenticated,]
    authentication_classes = []
    permission_classes = []
    serializer_class = NewFishSerializer
    # lookup_field = "user"
    
    def get_queryset(self): 
        user = self.request.user
        return FishingLogEntry.objects.filter(user=user)
    
    # def get_queryset(self):
    #     return FishingLogEntry.objects.filter(user=self.request.user)

class CreateLogEntry(generics.CreateAPIView):
    # authentication_classes = [FirebaseBackend]
    # permission_classes = [IsAuthenticated,]
    authentication_classes = []
    permission_classes = []
    queryset = FishingLogEntry.objects.all()
    serializer_class = NewFishSerializer
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

class EditOrDeleteLogEntry(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = FishingLogEntry.objects.all()
    serializer_class = CatchDataSerializer
    lookup_field = "id"
    
    def get_queryset(self):
        return FishingLogEntry.objects.filter(user=self.request.user)
    
    

    # updates catch using PUT http method, change it to patch
    
    


    
  