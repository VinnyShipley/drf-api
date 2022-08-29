from rest_framework import serializers
from .models import Donkey

class DonkeySerializer(serializers.ModelSerializer):
  class Meta:
    fields = ('id', 'owner', 'name', 'temperament', 'birth_info')
    model = Donkey
    