# Generated by Django 3.1.7 on 2021-04-09 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='guitar_model',
            field=models.CharField(max_length=35, null=True),
        ),
    ]