from rest_framework import serializers

from app.models import Ministry, District, Chapter, Event, Feedback


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
        model = Chapter
        fields = ('id', 'date', 'title', 'story', 'image', 'ministry', 'district')


class EventSerializer(serializers.ModelSerializer):
    ministry = MinistrySerializer()

    class Meta:
        model = Event
        fields = ('id', 'date', 'title', 'story', 'image', 'location', 'ministry')


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('id', 'title', 'content', 'date', 'time')
