# Generated by Django 5.0.2 on 2024-03-19 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_task_remindertime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='reminderTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
