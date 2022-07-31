# essence of the serialiser is just to define what
# data we want to serialise, that is : what data we 
# want to get from the datatbase and then return in json


from rest_framework import serializers
from trout.models import CatchData



class CatchDataSerializer(serializers.ModelSerializer):
    # define what data in the model you want to work with,
    # eg: you might not want to access all the fields
    class Meta:
        model = CatchData
        fields = ('id', 'user','river','river_pool','river_geotag',
                  'river_level','air_pressure','fish_species','fish_weight',
                  'fish_length','fish_condition','kept_or_released',
                  'fly_used','any_notes')
     
        
        

class NewFishSerializer(serializers.ModelSerializer):
    # define what data in the model you want to work with,
    # eg: you might not want to access all the field
    # date = serializers.DateField(format='iso-8601')
    class Meta:
        model = CatchData
        # 'dateTime'
        fields = ('id', 'date', 'river', 'river_pool', 'fish_species', 'fish_condition', 'fish_weight',
                  'fly_used','any_notes' , 'kept_or_released')
        
        
class SuperBasicSerializer(serializers.ModelSerializer):
    # define what data in the model you want to work with,
    # eg: you might not want to access all the fields
    class Meta:
        model = CatchData
        fields = ('id','river_pool','fly_used','any_notes')