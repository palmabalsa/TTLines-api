from rest_framework import generics
from firebase_admin import auth
from firebase_auth.authentication import FirebaseBackend
from trout.models import FishingLogEntry
from troutApi.serializers import CatchDataSerializer, NewFishSerializer, SuperBasicSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from users.serializers import UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class TrialEndPointFishList(generics.ListAPIView):
    authentication_classes = []
    # permission_classes = []
    permission_classes = ()
    serializer_class = NewFishSerializer
    queryset = FishingLogEntry.objects.all()
    
class TrialEditOrDeleteUser(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = ()
    queryset = FishingLogEntry.objects.all()
    serializer_class = UserSerializer
    lookup_field = "id"
    
    def get_queryset(self):
        djangoUser = self.request.user
        return User.objects.filter(firbase_user_id=djangoUser)    
    
class ListUsers(generics.ListAPIView):
    permission_classes = () 
    authentication_classes = []
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
    # def post(self, request, *args, **kwargs):
    #     print(request.user)   
    

class FishList(generics.ListAPIView):
    authentication_classes = [FirebaseBackend]
    permission_classes = [IsAuthenticated,]
    serializer_class = NewFishSerializer
    
    def get_queryset(self): 
        djangoUser = self.request.user
        return FishingLogEntry.objects.filter(user=djangoUser)
    


class CreateLogEntry(generics.CreateAPIView):
    authentication_classes = [FirebaseBackend]
    permission_classes = [IsAuthenticated, ]
    serializer_class = NewFishSerializer
    
    def perform_create(self, serializer):
        djangoUser = self.request.user
        return serializer.save(user=djangoUser)




class EditOrDeleteLogEntry(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [FirebaseBackend]
    permission_classes = [IsAuthenticated, ]
    serializer_class = CatchDataSerializer
    lookup_field = "id"
    
    def get_queryset(self): 
        djangoUser = self.request.user
        return FishingLogEntry.objects.filter(user=djangoUser)
    
    def perform_destroy(self, instance):
        instance = self.get_object()
        return super().perform_destroy(instance)
    
    def perform_update(self, serializer):
        instance = self.get_object()
        # djangoUser = self.request.user
        return super().perform_update(serializer)
    

    # updates catch using PUT http method, change it to patch


    
  