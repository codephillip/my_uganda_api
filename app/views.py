from rest_framework.decorators import api_view
from rest_framework.response import Response

from app.models import Ministry
from app.serializers import MinistrySerializer


@api_view(['GET'])
def get_ministrys(request, format=None):
    if request.method == 'GET':
        ministry = Ministry.objects.all()
        serializer = MinistrySerializer(ministry, many=True)
        return Response(serializer.data)
