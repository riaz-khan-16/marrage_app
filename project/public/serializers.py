
from rest_framework import serializers
from public.models import Intro

class IntroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intro
        fields = ['id', 'gender', 'mstatus', 'name', 'age', 'hometown','present_address','occupation','height','color','blood']


        
      

      