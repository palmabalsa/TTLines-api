from rest_framework import serializers
from users.models import User

class FireBaseAuthSerializer(serializers.Serializer):
    token = serializers.CharField()


class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=50, min_length=7, write_only=True)
    
    class Meta:
        model= User
        fields = ('email', 'username', 'password')
        
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
  
        
class LoginUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=50, min_length=7, write_only=True)
    class Meta:
        model = User
        fields = ('email', 'password', 'token')
        
        read_only_fields = ['token']  