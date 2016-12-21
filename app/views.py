from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app.models import Ministry, District, Chapter
from app.serializers import MinistrySerializer, DistrictSerializer, ChapterSerializer


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
