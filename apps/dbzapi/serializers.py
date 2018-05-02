from rest_framework import serializers
from .models import *


# serializers
class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ('pk', 'name')


class PlanetSerializer(serializers.HyperlinkedModelSerializer):
    location = serializers.HyperlinkedRelatedField(
        view_name='dbzapi:location_detail',
        read_only=True
    )

    class Meta:
        model = Planet
        fields = ('pk', 'name', 'destroyed', 'location')


class RaceSerializer(serializers.HyperlinkedModelSerializer):
    planet = serializers.HyperlinkedRelatedField(
        view_name='dbzapi:planet_detail',
        read_only=True
    )

    class Meta:
        model = Race
        fields = ('pk', 'name', 'planet')


class TechniqueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Technique
        fields = ('pk', 'name', 'description', 'damage')


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    race = serializers.HyperlinkedRelatedField(
        view_name='dbzapi:race_detail',
        read_only=True,
    )

    techniques = serializers.HyperlinkedRelatedField(
        view_name='dbzapi:technique_detail',
        many=True,
        read_only=True,
    )

    class Meta:
        model = Character
        fields = ('pk', 'name', 'fight_lvl', 'height', 'weight', 'race', 'techniques')
