# Generated by Django 2.0.13 on 2019-09-29 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20190929_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookactivitie',
            name='activity',
            field=models.CharField(choices=[('Checked Out', 'Checked Out'), ('Returned', 'Returned')], default=True, max_length=20),
        ),
    ]
