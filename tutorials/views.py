from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from .models import Komplekt, Music
from .serializers import KomplektSerializer, MusicSerializer
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



@api_view(['GET', 'POST', 'DELETE'])
def music_list(request):
    if request.method == 'GET':
        musics = Music.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            musics = musics.filter(title__icontains=title)

        musics_serializer = MusicSerializer(musics, many=True)
        return JsonResponse(musics_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        music_data = JSONParser().parse(request)
        music_serializer = MusicSerializer(data=music_data)
        if music_serializer.is_valid():
            music_serializer.save()
            return JsonResponse(music_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(music_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Music.objects.all().delete()
        return JsonResponse({'message': '{} Musics were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def music_detail(request, pk):
    try:
        music = Music.objects.get(pk=pk)
    except Music.DoesNotExist:
        return JsonResponse({'message': 'The music does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        music_serializer = MusicSerializer(music)
        return JsonResponse(music_serializer.data)

    elif request.method == 'PUT':
        music_data = JSONParser().parse(request)
        music_serializer = MusicSerializer(music, data=music_data)
        if music_serializer.is_valid():
            music_serializer.save()
            return JsonResponse(music_serializer.data)
        return JsonResponse(music_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        music.delete()
        return JsonResponse({'message': 'Music was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def music_list_published(request):
    musics = Music.objects.filter(published=True)

    if request.method == 'GET':
        musics_serializer = MusicSerializer(musics, many=True)
        return JsonResponse(musics_serializer.data, safe=False)

