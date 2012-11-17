from django.forms import widgets
from rest_framework import serializers
from BabyScheduleUi import models

class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Family
        fields = ('id', 'name')
    
class BabySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Baby
        fields = ('id', 'name', 'date_of_birth', 'family')
    
class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Activity
        fields = ('id', 'name', 'family')
    
class BabyEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BabyEvent
        fields = ('id', 'start_time', 'end_time', 'baby', 'activity')
    
class ActivityParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ActivityParameter
        fields = ('id', 'description', 'datatype', 'activity')
    
class EventDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EventData
        fields = ('id', 'data', 'baby_event', 'activity_parameters')
        
    