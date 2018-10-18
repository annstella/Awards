from rest_framework import serializers
from .models import ProfileMerch, ProjectsMerch

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileMerch
        fields = ('name', 'description')

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMerch
        fields = ('name', 'description')