# Generated by Django 2.1.7 on 2019-05-10 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstpractice', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='time',
            new_name='pub_date',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='content',
            new_name='title',
        ),
    ]
