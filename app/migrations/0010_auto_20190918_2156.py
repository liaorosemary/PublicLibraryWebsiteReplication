# Generated by Django 2.0.13 on 2019-09-18 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20190918_2148'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Books',
            new_name='Book',
        ),
        migrations.RenameModel(
            old_name='BookActivity',
            new_name='BookActivitie',
        ),
    ]
