# Generated by Django 2.0.13 on 2019-10-20 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20190929_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookactivitie',
            name='location',
            field=models.CharField(choices=[('New Sudbury Branch', 'New Sudbury Branch'), ('Garson Branch', 'Garson Branch'), ('Main', 'Main')], default=True, max_length=100),
        ),
    ]
