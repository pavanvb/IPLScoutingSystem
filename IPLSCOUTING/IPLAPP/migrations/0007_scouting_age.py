# Generated by Django 3.1.4 on 2020-12-13 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IPLAPP', '0006_t20stat'),
    ]

    operations = [
        migrations.AddField(
            model_name='scouting',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]
