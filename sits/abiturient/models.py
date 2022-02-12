from django.db import models
from django.utils.translation import gettext_lazy as _

class Header(models.Model):

    class Meta:
        verbose_name = _("Главная")
        verbose_name_plural = _("Главная")

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class HeadDis(models.Model):

    class Meta:
        verbose_name = _("Описание Главной страницы")
        verbose_name_plural = _("Описание Главной страницы")

    name = models.CharField(max_length=200)
    header = models.ForeignKey(Header,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Headerdis(models.Model):

    class Meta:
        verbose_name = _("Доп Главная")
        verbose_name_plural = _("Доп Главная")

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Quizzes(models.Model):
    class Meta:
        verbose_name = _("Quiz")
        verbose_name_plural = _("Quizzes")
        ordering = ['id']

    title = models.CharField(max_length=255, default=_("New Quiz"), verbose_name=_("Quiz Title"))
    category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Updated(models.Model):
    date_updated = models.DateTimeField(verbose_name=_("Last Updated"), auto_now=True)
    class Meta:
        abstract = True

class Question(Updated):
    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
        ordering = ['id']

    quiz = models.ForeignKey(Quizzes, related_name='question', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Created"))
    is_active = models.BooleanField(default=False, verbose_name=_("Active Status"))

    def __str__(self):
        return self.title

class Answer(Updated):
    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
        ordering = ['id']

    question = models.ForeignKey(Question, related_name='answer', on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=255, verbose_name=_("Answer Text"))
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text

class Career(models.Model):

    class Meta:
        verbose_name = _("Карьера")
        verbose_name_plural = _("Карьера")

    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Job_fair(models.Model):

    class Meta:
        verbose_name = _("Ярмарка вакансий")
        verbose_name_plural = _("Ярмарка вакансий")

    name = models.TextField()

    def __str__(self):
        return self.name

class Reception_campaign(models.Model):

    class Meta:
        verbose_name = _("Приемная")
        verbose_name_plural = _("Приемная")


    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Forms_of_training(models.Model):

    class Meta:
        verbose_name = _("Формы обучения")
        verbose_name_plural = _("Формы обучения")

    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Description_form(models.Model):

    class Meta:
        verbose_name = _("Описание формы обучения")
        verbose_name_plural = _("Описание формы обучения")

    form = models.ForeignKey(Forms_of_training,on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.description

class Open_day(models.Model):

    class Meta:
        verbose_name = _("День открытых дверей")
        verbose_name_plural = _("День открытых дверей")

    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name

class News_Blog(models.Model):

    class Meta:
        verbose_name = _("Новостной блог")
        verbose_name_plural = _("Новостной блог")

    name = models.CharField(max_length=300)
    date_created = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='images/',blank=True)

    def __str__(self):
        return self.name

class Connect(models.Model):

    class Meta:
        verbose_name = _("Связь")
        verbose_name_plural = _("Связь")

    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name

class File(models.Model):

    class Meta:
        verbose_name = _("Информация")
        verbose_name_plural = _("Информация")

    file = models.FileField(blank=False, null=False)

    def __str__(self):
        return self.file


