from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app.models import Ministry, District, Chapter, Event, Feedback
from app.serializers import MinistrySerializer, DistrictSerializer, ChapterSerializer, EventSerializer, \
    FeedbackSerializer


@api_view(['GET'])
def get_ministrys(request, format=None):
    try:
        ministrys = Ministry.objects.all()
    except Ministry.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MinistrySerializer(ministrys, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_ministry(request, pk, format=None):
    try:
        ministry = Ministry.objects.get(pk=pk)
        print(ministry)
    except Ministry.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MinistrySerializer(ministry)
        return Response(serializer.data)


@api_view(['GET'])
def get_districts(request, format=None):
    try:
        districts = District.objects.all()
    except District.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DistrictSerializer(districts, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_chapters(request, format=None):
    try:
        chapters = Chapter.objects.all()
        print("chapters#")
        print(chapters)
    except Chapter.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ChapterSerializer(chapters, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_events(request, format=None):
    try:
        events = Event.objects.all()
        print("events#")
        print(events)
    except Event.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def post_feedback(request):
    print("posting#")
    # checking sent data directly from request
    # print(request.data)
    # print(request.data['content'])
    serializer = FeedbackSerializer(data=request.data)
    if serializer.is_valid():
        # checking sent data after serialization
        # print(serializer.validated_data['title'])
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_feedbacks(request, format=None):
    try:
        feedbacks = Feedback.objects.all()
    except Feedback.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = FeedbackSerializer(feedbacks, many=True)
        return Response(serializer.data)
