# Generated by Django 4.0.3 on 2022-04-26 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_area', '0014_lesson_visible'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='visible',
        ),
    ]