# Generated by Django 5.0 on 2023-12-29 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateTimeField(default='2001-04-14'),
            preserve_default=False,
        ),
    ]
