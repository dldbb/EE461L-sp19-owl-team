# Generated by Django 2.1.7 on 2019-02-22 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ecoregion',
            name='photo',
            field=models.ImageField(default='ecoregions', upload_to='ecoregions'),
        ),
        migrations.AddField(
            model_name='plant',
            name='photo',
            field=models.ImageField(default='stateparks', upload_to='plants'),
        ),
        migrations.AddField(
            model_name='statepark',
            name='photo',
            field=models.ImageField(default='stateparks', upload_to='stateparks'),
        ),
    ]
