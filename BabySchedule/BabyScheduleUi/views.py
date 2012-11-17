from django.http import HttpResponse
from BabyScheduleUi.models import Family
from BabyScheduleUi.serializers import FamilySerializer
from rest_framework import generics

def home(request):
    return HttpResponse("Hello, world. You're at BabySchedule home.")

class FamilyList(generics.ListCreateAPIView):
    """
    List all families, or create a new family
    """
    model = Family
    serializer_class = FamilySerializer
    
class FamilyDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a family 
    """
    model = Family
    serializer_class = FamilySerializer
