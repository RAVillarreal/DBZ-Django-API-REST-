from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *


# Create your views here.
class CharacterList(APIView):
    def get(self, request):
        characters = Character.objects.all()
        return Response(
            CharacterSerializer(characters, context={'request': request}, many=True).data,
            status=status.HTTP_200_OK
        )


class CharacterDetail(APIView):
    def get_object(self, pk):
        try:
            return Character.objects.get(pk=pk)
        except Character.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        character = Character.objects.filter(pk=pk)
        return Response(
            RaceSerializer(character, context={'request': request}).data,
            status=status.HTTP_200_OK
        )

    def post(self, request):
        serializer = CharacterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RaceDetail(APIView):
    def get_object(self, pk):
        try:
            return Race.objects.get(pk=pk)
        except Race.DoesNotExist:
            raise Http404


    def get(self, request, pk):
        race = Race.objects.filter(pk=pk)
        return Response(
            RaceSerializer(race, context={'request': request}).data,
            status=status.HTTP_200_OK
        )

    def post(self, request):
        serializer = RaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlanetDetail(APIView):
    def get_object(self, pk):
        try:
            return Planet.objects.get(pk=pk)
        except Planet.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        planet = Planet.objects.filter(pk=pk)
        return Response(
            PlanetSerializer(planet, context={'request': request}).data,
            status=status.HTTP_200_OK
        )

    def post(self, request):
        serializer = PlanetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TechniqueDetail(APIView):
    def get_object(self, pk):
        try:
            return Technique.objects.get(pk=pk)
        except Technique.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        technique = Technique.objects.filter(pk=pk)
        return Response(
            TechniqueSerializer(technique, context={'request': request}).data,
            status=status.HTTP_200_OK
        )

    def post(self, request):
        serializer = TechniqueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LocationDetail(APIView):
    def get_object(self, pk):
        try:
            return Location.objects.get(pk=pk)
        except Location.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        location = Location.objects.filter(pk=pk)
        return Response(
            LocationSerializer(location, context={'request': request}).data,
            status=status.HTTP_200_OK
        )

    def post(self, request):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
