from django.shortcuts import render
from .models import Donkey
from .serializers import DonkeySerializer
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

class DonkeyList(ListCreateAPIView):
  queryset = Donkey.objects.all()
  serializer_class = DonkeySerializer
  
class DonkeyDetail(RetrieveDestroyAPIView):
  queryset = Donkey.objects.all()
  serializer_class = DonkeySerializer


