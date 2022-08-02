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
        
        
# class RegisterUserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(max_length=50, min_length=7, write_only=True)
    
#     class Meta:
#         model= User
#         fields = ('email', 'username', 'password')
#                 #   'first_name', 'last_name',)
        
#     def create(self, validated_data):
#         return User.objects.create_user(**validated_data)
#         # password = validated_data.pop('password', None)
#         # instance = self.Meta.model(**validated_data)
#         # if password is not None:
#         #     instance.set_password(password)
#         # instance.save()
#         # return instance    