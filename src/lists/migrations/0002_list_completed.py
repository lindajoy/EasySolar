# Generated by Django 2.2 on 2020-08-16 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
