from rest_framework import generics
from trout.models import FishingLogEntry
from troutApi.serializers import CatchDataSerializer, NewFishSerializer, SuperBasicSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny


# test endpoint displaying all data without loggin in
class TrialEndPointFishList(generics.ListAPIView):
    authentication_classes = []
    permission_classes = (AllowAny,)
    serializer_class = NewFishSerializer
    queryset = FishingLogEntry.objects.all()

class FishList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = NewFishSerializer
    
    def get_queryset(self):
        return FishingLogEntry.objects.filter(user=self.request.user)

class CreateLogEntry(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
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
    
    


    
  