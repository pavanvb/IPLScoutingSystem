# Generated by Django 3.1.4 on 2020-12-14 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IPLAPP', '0020_auto_20201214_2250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='odistat',
            name='odi',
        ),
        migrations.RemoveField(
            model_name='t20stat',
            name='t20',
        ),
        migrations.DeleteModel(
            name='T20STATI',
        ),
        migrations.DeleteModel(
            name='Teststat',
        ),
        migrations.DeleteModel(
            name='Odistat',
        ),
        migrations.DeleteModel(
            name='T20Stat',
        ),
    ]