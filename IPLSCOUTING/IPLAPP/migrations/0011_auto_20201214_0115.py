# Generated by Django 3.1.4 on 2020-12-13 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IPLAPP', '0010_auto_20201214_0055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='id',
        ),
        migrations.AddField(
            model_name='player',
            name='Player_id',
            field=models.CharField(default=0, max_length=50, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
