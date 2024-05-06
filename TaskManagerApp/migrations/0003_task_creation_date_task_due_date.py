# Generated by Django 5.0.4 on 2024-05-06 05:07

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskManagerApp', '0002_task_text_task_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='creation date'),
        ),
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(null=True, verbose_name='due date'),
        ),
    ]
