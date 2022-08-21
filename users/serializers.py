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