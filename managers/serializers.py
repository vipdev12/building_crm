from rest_framework import serializers

from .models import Manager


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ['full_name', 'phone_number',
                  'email', 'password']