from rest_framework import serializers
from .models import *


class HeaderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = '__all__'

class HeadDisSerializer(serializers.ModelSerializer):
    head = HeaderSerializers(read_only=True,many=True)
    class Meta:
        model = HeadDis
        fields = '__all__'

class HeaderdisSerialzers(serializers.ModelSerializer):
    class Meta:
        model = Headerdis
        fields = '__all__'

class ContactSerailizer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    subject = serializers.CharField()
    message = serializers.CharField()

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quizzes
        fields = [
            'title',
        ]

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = [
            'id',
            'answer_text',
        ]

class RandomQuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = [
            'title', 'answer',
        ]

class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True)
    quiz = QuizSerializer(read_only=True)
    class Meta:
        model = Question
        fields = [
            'quiz', 'title', 'answer',
        ]

class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = '__all__'

class JobfairSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job_fair
        fields = '__all__'

class Reception_campaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reception_campaign
        fields = '__all__'

class Forms_of_trainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forms_of_training
        fields = '__all__'


class Description_formSerializer(serializers.ModelSerializer):
    form = Forms_of_trainingSerializer(read_only=True)
    class Meta:
        model = Description_form
        fields = '__all__'

class Open_daySerializer(serializers.ModelSerializer):
    class Meta:
        model = Open_day
        fields = '__all__'

class News_blogSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=False, use_url=True, required=False)
    class Meta:
        model = News_Blog
        fields = '__all__'

class ConnectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connect
        fields = '__all__'

class FileSerializer(serializers.ModelSerializer):
  class Meta():
    model = File
    fields = '__all__'
