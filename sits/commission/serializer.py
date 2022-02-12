from rest_framework import serializers
from .models import *

class CommissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commission
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = '__all__'

class ParagraphDisSerializer(serializers.ModelSerializer):
    paragraph = ParagraphSerializer(read_only=True,many=True)

    class Meta:
        model = ParagraphDis
        fields = '__all__'

class Open_daySerializer(serializers.ModelSerializer):
    class Meta:
        model = Open_day
        fields = '__all__'
