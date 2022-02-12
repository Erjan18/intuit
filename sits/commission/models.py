from django.db import models
from django.utils.translation import gettext_lazy as _


class Commission(models.Model):

    class Meta:
        verbose_name = _("Приемная комиссия")
        verbose_name_plural = _("Приемная комиссия")

    name = models.TextField()

    def __str__(self):
        return self.name

class Contact(models.Model):

    class Meta:
        verbose_name = _("Контакты приемной комиссии")
        verbose_name_plural = _("Контакты приемной комиссии")

    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name

class Paragraph(models.Model):

    class Meta:
        verbose_name = _("Пункты")
        verbose_name_plural = _("Пункты")

    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class ParagraphDis(models.Model):

    class Meta:
        verbose_name = _("Описание пунктов")
        verbose_name_plural = _("Описание пунктов")

    paragraph = models.ForeignKey(Paragraph,on_delete=models.CASCADE)
    name = models.TextField()

    def __str__(self):
        return self.name

class Open_day(models.Model):

    class Meta:
        verbose_name = _("День открытых дверей")
        verbose_name_plural = _("День открытых дверей")

    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name