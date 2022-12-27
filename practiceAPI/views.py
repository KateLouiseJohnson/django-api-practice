from django.http import JsonResponse
from .models import Data
from .serializers import DataSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def data(request):
    if request.method == 'GET':
        data = Data.objects.all()
        serializer = DataSerializer(data, many=True)
        return Response({'datas': serializer.data})
    elif request.method == 'POST':
        serializer = DataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def data_by_id(request, id):
    try:
        data = Data.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    if request.method == 'GET':
        serializer = DataSerializer(data)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DataSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def landing(request):
    return JsonResponse('Welcome', safe=False)
