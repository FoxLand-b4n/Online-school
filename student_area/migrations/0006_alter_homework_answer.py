# Generated by Django 4.0.3 on 2022-04-16 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_area', '0005_remove_homework_file_name_alter_homework_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='answer',
            field=models.FileField(upload_to=''),
        ),
    ]
