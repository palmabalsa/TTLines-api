from rest_framework import serializers
from trout.models import FishingLogEntry

class CatchDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FishingLogEntry
        fields = ('id', 'user','date','region', 'river','river_pool','lat', 'lon',
                  'river_level','air_pressure','fish_species','fish_weight', 'image',
                  'fish_length','fish_condition','kept_or_released',
                  'fly_used','any_notes', 'number_of_fish')
     
class NewFishSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='User.firebase_user_id')
    class Meta:
        model = FishingLogEntry
        fields = ('user', 'id', 'date', 'region', 'river', 'river_pool', 'lat', 'lon', 'fish_species', 'fish_condition', 'fish_weight', 'image', 'fly_used','any_notes' , 'kept_or_released', 'number_of_fish')


class FishPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FishingLogEntry
        fields = ('user', 'id', 'image', 'fish_species', 'fish_weight')

    
class SuperBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = FishingLogEntry
        fields = ('id','river_pool','fly_used','any_notes')