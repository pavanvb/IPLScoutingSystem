# Generated by Django 3.1.4 on 2020-12-14 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IPLAPP', '0015_auto_20201214_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='odistat',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='t20stat',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teststat',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='odistat',
            name='odi',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='IPLAPP.player', unique=True),
        ),
        migrations.AlterField(
            model_name='t20stat',
            name='t20',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='IPLAPP.player', unique=True),
        ),
        migrations.AlterField(
            model_name='teststat',
            name='test',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='IPLAPP.player', unique=True),
        ),
    ]
