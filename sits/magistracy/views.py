from django.shortcuts import render
from rest_framework import status
from .serializer import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response


class MagistracyView(APIView):
    def get(self,*args,**kwargs):
        name = Magistracy.objects.all()
        serializer = MagistracySerializer(name,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class FormstrainingrView(APIView):
    def get(self,*args,**kwargs):
        name = Forms_training.objects.all()
        serializer = FormstrainingSerializer(name,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class Oplata_zaView(APIView):
    def get(self,*args,**kwargs):
        name = Oplata_za.objects.all()
        serializer = Oplata_zaSerializer(name,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class DiscountView(APIView):
    def get(self,*args,**kwargs):
        name = Discount.objects.all()
        serializer = DiscountSerializer(name,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class TransferView(APIView):
    def get(self,*args,**kwargs):
        name = Transfer.objects.all()
        serializer = TransferSerializer(name,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class AvailabilityView(APIView):
    def get(self,*args,**kwargs):
        name = Availability.objects.all()
        serializer = AvailabilitySerializer(name,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class JobmagistView(APIView):
    def get(self,*args,**kwargs):
        name = Jobmagis.objects.all()
        serializer = JobmagisSerializer(name,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class EnactusView(APIView):
    def get(self,*args,**kwargs):
        name = Enactus.objects.all()
        serializer = EnactusSerializer(name,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class DescriptionView(APIView):
    def get(self,*args,**kwargs):
        name = Description.objects.all()
        serializer = DescriptionSerializer(name,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class CatalogView(APIView):
    def get(self,*args,**kwargs):
        name = Catalog.objects.all()
        serializer = CatalogSerializer(name,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)