from rest_framework import serializers
from .models import Memu

class MemuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Memu # 모델 설정
        fields = ('item','size','price','temp','cover') # 필드 설정