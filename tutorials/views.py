from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from .models import Komplekt
from .serializers import KomplektSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def komplekt_list(request):
    if request.method == 'GET':
        komplekts = Komplekt.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            komplekts = komplekts.filter(title__icontains=title)
        
        komplekts_serializer = KomplektSerializer(komplekts, many=True)
        return JsonResponse(komplekts_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        komplekt_data = JSONParser().parse(request)
        komplekt_serializer = KomplektSerializer(data=komplekt_data)
        if komplekt_serializer.is_valid():
            komplekt_serializer.save()
            return JsonResponse(komplekt_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(komplekt_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Komplekt.objects.all().delete()
        return JsonResponse({'message': '{} Komplekts were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def komplekt_detail(request, pk):
    try: 
        komplekt = Komplekt.objects.get(pk=pk)
    except Komplekt.DoesNotExist:
        return JsonResponse({'message': 'The komplekt does not exist'}, status=status.HTTP_404_NOT_FOUND)
 
    if request.method == 'GET': 
        komplekt_serializer = KomplektSerializer(komplekt)
        return JsonResponse(komplekt_serializer.data)
 
    elif request.method == 'PUT': 
        komplekt_data = JSONParser().parse(request)
        komplekt_serializer = KomplektSerializer(komplekt, data=komplekt_data)
        if komplekt_serializer.is_valid():
            komplekt_serializer.save()
            return JsonResponse(komplekt_serializer.data)
        return JsonResponse(komplekt_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    elif request.method == 'DELETE': 
        komplekt.delete()
        return JsonResponse({'message': 'Komplekt was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def komplekt_list_published(request):
    komplekts = Komplekt.objects.filter(published=True)
        
    if request.method == 'GET': 
        komplekts_serializer = KomplektSerializer(komplekts, many=True)
        return JsonResponse(komplekts_serializer.data, safe=False)
