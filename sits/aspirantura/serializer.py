from rest_framework import serializers
from .models import *

class AspiranturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aspirantura
        fields = '__all__'

class FormstrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forms_training
        fields = '__all__'

class Oplata_zaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oplata_za
        fields = '__all__'

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'

class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = '__all__'

class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = '__all__'

class JobspirantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobspirant
        fields = '__all__'

class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = '__all__'

class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = '__all__'