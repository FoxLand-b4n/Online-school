# Generated by Django 4.0.3 on 2022-04-29 22:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_area', '0017_alter_test_what_lesson'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='what_test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_area.test'),
        ),
    ]