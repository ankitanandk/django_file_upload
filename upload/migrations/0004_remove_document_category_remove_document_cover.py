# Generated by Django 4.0.6 on 2022-08-03 03:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0003_rename_book_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='category',
        ),
        migrations.RemoveField(
            model_name='document',
            name='cover',
        ),
    ]
