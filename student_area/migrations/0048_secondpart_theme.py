# Generated by Django 4.0.3 on 2022-05-02 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_area', '0047_secondpart_homeworksecondpart'),
    ]

    operations = [
        migrations.AddField(
            model_name='secondpart',
            name='theme',
            field=models.CharField(default=0, max_length=500),
        ),
    ]
