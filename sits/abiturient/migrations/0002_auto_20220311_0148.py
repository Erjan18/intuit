# Generated by Django 3.1.3 on 2022-03-10 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('abiturient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(blank=True, upload_to='file'),
        ),
        migrations.AlterField(
            model_name='headdis',
            name='header',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hamer', to='abiturient.header'),
        ),
        migrations.DeleteModel(
            name='Abiturientdis',
        ),
    ]
