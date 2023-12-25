from rest_framework import serializers
from .models import pizzeria


class pizzeriaListSerializer(serializers.ModelSerializer):
    class Meta:
        model= pizzeria
        fields=[
            'id',
            'pizzaria_name',
            'city',
            'zip_code',
            
        ]
        
class pizzeriaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model= pizzeria
        fields=[
            'id',
            'pizzaria_name',
            'city',
            'state',
            'zip_code',
            'website',
            'phone_number',
            'description',
            'logo_image',
            'email',
            'active',
        ]