# Generated by Django 3.2.4 on 2021-06-21 02:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_alter_task_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
