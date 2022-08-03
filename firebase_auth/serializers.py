from rest_framework import serializers
from users.models import User

class FireBaseAuthSerializer(serializers.Serializer):
    token = serializers.CharField()