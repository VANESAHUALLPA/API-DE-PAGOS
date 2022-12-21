from rest_framework import serializers
from .models import Pagos2 

class Pago2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Pagos2
        fields = '__all__'
        read_only_fields = '__all__',