# Generated by Django 5.0.4 on 2024-05-06 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskManagerApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='text',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='task',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]