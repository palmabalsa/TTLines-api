from rest_framework import serializers
from trout.models import FishingLogEntry

class CatchDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FishingLogEntry
        fields = ('id', 'user','river','river_pool','river_geotag',
                  'river_level','air_pressure','fish_species','fish_weight',
                  'fish_length','fish_condition','kept_or_released',
                  'fly_used','any_notes')
     

class NewFishSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    class Meta:
        model = FishingLogEntry
        fields = ('user', 'id', 'date', 'river', 'river_pool', 'fish_species', 'fish_condition', 'fish_weight',
                  'fly_used','any_notes' , 'kept_or_released')
    
    
    # these methods are already defined by using a model serializer so no need for them
    # def create(self, validated_data):
    #     return FishingLogEntry.objects.create(**validated_data)
    
    # def update(self, instance, **validated_data):
    #     instance.date = validated_data.get('date', instance.date)
    #     instance.river = validated_data.get('river', instance.river)
    #     instance.river_pool = validated_data.get('river_pool', instance.river_pool)
    #     instance.fish_species = validated_data.get('fish_species', instance.fish_species)
    #     instance.fish_condition = validated_data.get('fish_condition', instance.fish_condition)
    #     instance.fish_weight = validated_data.get('fish_weight', instance.fish_weight)
    #     instance.fly_used = validated_data.get('fly_used', instance.fly_used)
    #     instance.any_notes = validated_data.get('any_notes', instance.any_notes)
    #     instance.kept_or_released = validated_data.get('kept_or_released', instance.kept_or_released)
    
    #     instance.save()
    #     return instance
        
        
        
class SuperBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = FishingLogEntry
        fields = ('id','river_pool','fly_used','any_notes')