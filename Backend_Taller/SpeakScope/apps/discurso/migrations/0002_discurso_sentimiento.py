# Generated by Django 4.2.5 on 2023-12-14 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discurso', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='discurso',
            name='sentimiento',
            field=models.TextField(null=True),
        ),
    ]
