# Generated by Django 4.0.3 on 2022-04-21 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_area', '0009_rename_created_answer_data_created_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='right_or_not',
        ),
        migrations.AddField(
            model_name='choice',
            name='right_or_not',
            field=models.BooleanField(default=None),
        ),
    ]