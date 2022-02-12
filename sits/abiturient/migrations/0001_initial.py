# Generated by Django 3.1.3 on 2022-02-12 00:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': 'Карьера',
                'verbose_name_plural': 'Карьера',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Connect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
            ],
            options={
                'verbose_name': 'Связь',
                'verbose_name_plural': 'Связь',
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
            options={
                'verbose_name': 'Информация',
                'verbose_name_plural': 'Информация',
            },
        ),
        migrations.CreateModel(
            name='Forms_of_training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'Формы обучения',
                'verbose_name_plural': 'Формы обучения',
            },
        ),
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Главная',
                'verbose_name_plural': 'Главная',
            },
        ),
        migrations.CreateModel(
            name='Headerdis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Доп Главная',
                'verbose_name_plural': 'Доп Главная',
            },
        ),
        migrations.CreateModel(
            name='Job_fair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
            options={
                'verbose_name': 'Ярмарка вакансий',
                'verbose_name_plural': 'Ярмарка вакансий',
            },
        ),
        migrations.CreateModel(
            name='News_Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('photo', models.ImageField(blank=True, upload_to='images/')),
            ],
            options={
                'verbose_name': 'Новостной блог',
                'verbose_name_plural': 'Новостной блог',
            },
        ),
        migrations.CreateModel(
            name='Open_day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
            ],
            options={
                'verbose_name': 'День открытых дверей',
                'verbose_name_plural': 'День открытых дверей',
            },
        ),
        migrations.CreateModel(
            name='Reception_campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': 'Приемная',
                'verbose_name_plural': 'Приемная',
            },
        ),
        migrations.CreateModel(
            name='Quizzes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='New Quiz', max_length=255, verbose_name='Quiz Title')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='abiturient.category')),
            ],
            options={
                'verbose_name': 'Quiz',
                'verbose_name_plural': 'Quizzes',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('is_active', models.BooleanField(default=False, verbose_name='Active Status')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='abiturient.quizzes')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='HeadDis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abiturient.header')),
            ],
            options={
                'verbose_name': 'Описание Главной страницы',
                'verbose_name_plural': 'Описание Главной страницы',
            },
        ),
        migrations.CreateModel(
            name='Description_form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abiturient.forms_of_training')),
            ],
            options={
                'verbose_name': 'Описание формы обучения',
                'verbose_name_plural': 'Описание формы обучения',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('answer_text', models.CharField(max_length=255, verbose_name='Answer Text')),
                ('is_right', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='abiturient.question')),
            ],
            options={
                'verbose_name': 'Answer',
                'verbose_name_plural': 'Answers',
                'ordering': ['id'],
            },
        ),
    ]
