from django.db import models
from django.utils.translation import gettext_lazy as _

class Aspirantura(models.Model):

    class Meta:
        verbose_name = _("Аспирантура")
        verbose_name_plural = _("Аспирантура")

    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name

class Forms_training(models.Model):

    class Meta:
        verbose_name = _("Формы обучения")
        verbose_name_plural = _("Формы обучения")

    name = models.TextField()

    def __str__(self):
        return self.name

class Oplata_za(models.Model):

    class Meta:
        verbose_name = _("Оплата обучения онлайн")
        verbose_name_plural = _("Оплата обучения онлайн")

    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name

class Discount(models.Model):

    class Meta:
        verbose_name = _("Скидки на обучения")
        verbose_name_plural = _("Скидки на обучения")

    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name

class Transfer(models.Model):

    class Meta:
        verbose_name = _("Перевод из другого вуза")
        verbose_name_plural = _("Перевод из другого вуза")

    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name

class Availability(models.Model):

    class Meta:
        verbose_name = _("Доступность учебных материалов")
        verbose_name_plural = _("Доступность учебных материалов")

    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name

class Jobspirant(models.Model):

    class Meta:
        verbose_name = _("Трудоустройство аспирантов")
        verbose_name_plural = _("Трудоустройство аспирантов")

    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name


class Description(models.Model):

    class Meta:
        verbose_name = _("Описание")
        verbose_name_plural = _("Описание")

    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name

class Catalog(models.Model):

    class Meta:
        verbose_name = _("Каталог Университета МУИТ")
        verbose_name_plural = _("Каталог Университета МУИТ")

    name = models.CharField(max_length=400)
    file = models.FileField(upload_to='file',blank=True)

    def __str__(self):
        return self.name