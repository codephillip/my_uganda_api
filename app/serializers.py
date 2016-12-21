from rest_framework import serializers

from app.models import Ministry, District


class MinistrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ministry
        fields = ('id', 'name', 'image')


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ('id', 'name', 'region')


class ChapterSerializer(serializers.ModelSerializer):
    ministry = MinistrySerializer()
    district = DistrictSerializer()

    class Meta:
        model = District
        # fix 'date'
        fields = ('id', 'title', 'story', 'image', 'ministry', 'district')
