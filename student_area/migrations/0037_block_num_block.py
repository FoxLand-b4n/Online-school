# Generated by Django 4.0.3 on 2022-04-30 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_area', '0036_result_status_check'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='num_block',
            field=models.IntegerField(default=0),
        ),
    ]