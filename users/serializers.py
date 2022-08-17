from rest_framework import serializers
from trout.models import FishingLogEntry
from users.models import User


class UserSerializer(serializers.ModelSerializer):
        # log_entries = serializers.PrimaryKeyRelatedField(many=True, queryset=FishingLogEntry.objects.all())
        class Meta:
                model = User
                fields = '__all__'
                # fields = ['email', 'firebase_user_id']
                # 'log_entries'
        
        
        
        
        

# class FireBaseAuthSerializer(serializers.Serializer):
#     token = serializers.CharField()


# class RegisterUserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(max_length=50, min_length=7, write_only=True)
    
#     class Meta:
#         model= User
#         fields = ('email', 'username', 'password')
        
#     def create(self, validated_data):
#         return User.objects.create_user(**validated_data)
  
        
# class LoginUserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(max_length=50, min_length=7, write_only=True)
#     class Meta:
#         model = User
#         fields = ('email', 'password')
        # fields = ('email', 'password', 'token')
        
        # read_only_fields = ['token']  