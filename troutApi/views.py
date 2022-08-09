from rest_framework import generics
from firebase_auth.authentication import FirebaseBackend
from trout.models import FishingLogEntry
from troutApi.serializers import CatchDataSerializer, NewFishSerializer, SuperBasicSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
# from firebase_admin import auth
# from django.contrib.auth import get_user_model

# test endpoint displaying all data without loggin in
class TrialEndPointFishList(generics.ListAPIView):
    authentication_classes = []
    # permission_classes = []
    permission_classes = (AllowAny,)
    serializer_class = NewFishSerializer
    queryset = FishingLogEntry.objects.all()

class FishList(generics.ListAPIView):
    authentication_classes = [FirebaseBackend,]
    permission_classes = [IsAuthenticated,]
    serializer_class = NewFishSerializer
    
    def get_queryset(self):
        return FishingLogEntry.objects.filter(user=self.request.user)

class CreateLogEntry(generics.CreateAPIView):
    authentication_classes = [FirebaseBackend]
    permission_classes = [IsAuthenticated,]
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
    
    


    
  