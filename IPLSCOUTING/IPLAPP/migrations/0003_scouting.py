# Generated by Django 3.1.4 on 2020-12-13 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IPLAPP', '0002_auto_20201213_2237'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scouting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
