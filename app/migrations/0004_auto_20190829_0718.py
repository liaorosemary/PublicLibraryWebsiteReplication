# Generated by Django 2.0.13 on 2019-08-29 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_books_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='description',
            field=models.TextField(blank=True, max_length=2000),
        ),
    ]
