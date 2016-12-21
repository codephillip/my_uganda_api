from rest_framework import serializers

from app.models import Ministry


class MinistrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ministry
        fields = ('id', 'name', 'image')
