from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializer import *


class CommissionView(APIView):
    def get(self,*args,**kwargs):
        name = Commission.objects.all()
        serializer = CommissionSerializer(name,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class ContactView(APIView):
    def get(self,*args,**kwargs):
        name = Contact.objects.all()
        serializer = ContactSerializer(name,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class ParagraphView(APIView):
    def get(self,*args,**kwargs):
        name = Paragraph.objects.all()
        serializer = ParagraphSerializer(name,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class ParagraphDisView(APIView):
    def get(self,*args,**kwargs):
        name = ParagraphDis.objects.all()
        serializer = ParagraphDisSerializer(name,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class OpendayView(APIView):
    def get(self,*args,**kwargs):
        name = Open_day.objects.all()
        serializer = Open_daySerializer(name,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

