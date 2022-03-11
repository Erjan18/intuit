from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets,permissions,generics
from rest_framework.viewsets import ModelViewSet
from django.views.generic import CreateView
from django.core.mail import send_mail
from rest_framework.parsers import MultiPartParser, FormParser

class HeadView(APIView):
    def get(self,*args,**kwargs):
        name = Header.objects.all()
        serializer = HeaderSerializers(name,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class HeaderView(APIView):
    def get(self,*args,**kwargs):
        name = HeadDis.objects.all()
        serializer = HeadDisSerializer(name,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class HeadisView(viewsets.ModelViewSet):
    def get(self,*args,**kwargs):
        name= Headerdis.objects.all()
        serializer = HeaderdisSerialzers(name,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class FeedBackView(APIView):
    serializer_class = ContactSerailizer

    def post(self, request, *args, **kwargs):
        try:
            serializer_class = ContactSerailizer(data=request.data)
            if serializer_class.is_valid():
                data = serializer_class.validated_data
                name = data.get('name')
                from_email = data.get('email')
                subject = data.get('subject')
                message = data.get('message')
                send_mail(f'От {name} | {subject}',message, from_email, ['intuitkg2020@gmail.com'])
                return Response("Succes:Sent")
            else:
                return Response("Failed to Send")
        except Exception as err:
            return Response({err})

class Quiz(APIView):

    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()

class RandomQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(quiz__title=kwargs['topic']).order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)

    def filter(self):
        if RandomQuestionSerializer.fields == 'Гуманитарным':
             return Response('Гуманитарным')
        elif RandomQuestionSerializer.fields == 'Техническим':
            return Response('Техническим')
        if RandomQuestionSerializer.fields == 'Колледж':
            return Response('Колледж')
        elif RandomQuestionSerializer == 'Бакалавриат':
            return Response('Бакалавриат')
        elif RandomQuestionSerializer.fields == 'Аспирантура':
            return Response('Аспирантура')
        elif RandomQuestionSerializer.fields == 'Магистратура':
            return Response('Магистратура')

class QuizQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        quiz = Question.objects.filter(quiz__title=kwargs['topic'])
        serializer = QuestionSerializer(quiz, many=True)
        return Response(serializer.data)

class CareerView(APIView):
    def get(self,*args,**kwargs):
        name = Career.objects.all()
        serializer = CareerSerializer(name,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class Job_fairView(APIView):
    def get(self,*args,**kwargs):
        name = Job_fair.objects.all()
        serializer = JobfairSerializer(name,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class Reception_campaignView(APIView):
    def get(self,*args,**kwargs):
        name = Reception_campaign.objects.all()
        serializer = Reception_campaignSerializer(name,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class Forms_of_trainingView(APIView):
    def get(self,*args,**kwargs):
        name = Forms_of_training.objects.all()
        serializer = Forms_of_trainingSerializer(name,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class Description_formView(APIView):
    def get(self,*args,**kwargs):
        name = Description_form.objects.all()
        serializer = Description_formSerializer(name,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class Open_dayView(APIView):
    def get(self,*args,**kwargs):
        name = Open_day.objects.all()
        serializer = Open_daySerializer(name,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class News_blogView(APIView):
    def get(self,*args,**kwargs):
        name = News_Blog.objects.all()
        serializer = News_blogSerializer(name,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class ConnectView(APIView):
    def get(self,*args,**kwargs):
        name = Connect.objects.all()
        serializer = ConnectSerializer(name,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class FileView(APIView):
    def get(self, request, *args, **kwargs):
        name = File.objects.all()
        file_serializer = FileSerializer(name,data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
        return Response(file_serializer.data, status=status.HTTP_200_OK)

class AbiturientView(APIView):
    def get(self, request, *args, **kwargs):
        name = Abiturient.objects.all()
        serializer = AbiturientSerializers(name, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CenterView(APIView):
    def get(self, request, *args, **kwargs):
        name = Center_carrer.objects.all()
        serializer = CenterSerializers(name, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class StudentView(APIView):
    def get(self, request, *args, **kwargs):
        name = Student.objects.all()
        serializer = StudentSerializers(name, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class EnactusView(APIView):
    def get(self, request, *args, **kwargs):
        name = Enactus.objects.all()
        serializer = EnactusSerializers(name, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AboutView(APIView):
    def get(self, request, *args, **kwargs):
        name = About.objects.all()
        serializer = AboutSerializers(name, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)