# Generated by Django 5.0.6 on 2024-06-12 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documents',
            name='filename',
        ),
    ]
