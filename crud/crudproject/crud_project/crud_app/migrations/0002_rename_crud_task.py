# Generated by Django 4.2.2 on 2023-06-08 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Crud',
            new_name='Task',
        ),
    ]