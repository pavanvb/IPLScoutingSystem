# Generated by Django 3.1.4 on 2020-12-14 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IPLAPP', '0013_auto_20201214_0121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='Player_id',
        ),
        migrations.AddField(
            model_name='odistat',
            name='ODImatches',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='t20stat',
            name='t20matches',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='teststat',
            name='Testmatches',
            field=models.IntegerField(default=0),
        ),
    ]
