# Generated by Django 4.0.3 on 2022-04-30 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_area', '0033_everyquestionchoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_area.test'),
        ),
    ]