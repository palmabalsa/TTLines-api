from rest_framework import serializers
from users.models import User

class FireBaseAuthSerializer(serializers.Serializer):
    token = serializers.CharField()

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ('email', 'first_name', 'last_name', 'username', 'password')
        
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance     