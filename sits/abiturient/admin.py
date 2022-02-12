from django.contrib import admin
from . import models
from .models import Headerdis,Career,Job_fair,Reception_campaign,Forms_of_training,Description_form,Open_day,News_Blog,Connect,File
from .models import Header,HeadDis

admin.site.register([Header,HeadDis,Headerdis,Career,Job_fair,Reception_campaign,Forms_of_training,Description_form,
                     Open_day,News_Blog,Connect,File])

class Contact(admin.ModelAdmin):
    list_display = ('last_name','number','mail')

@admin.register(models.Category)

class CatAdmin(admin.ModelAdmin):
	list_display = [
        'name',
        ]

@admin.register(models.Quizzes)

class QuizAdmin(admin.ModelAdmin):
	list_display = [
        'id',
        'title',
        ]

class AnswerInlineModel(admin.TabularInline):
    model = models.Answer
    fields = [
        'answer_text',
        'is_right'
        ]

@admin.register(models.Question)

class QuestionAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'quiz',
        ]
    list_display = [
        'title',
        'quiz',
        'date_updated'
        ]
    inlines = [
        AnswerInlineModel,
        ]

