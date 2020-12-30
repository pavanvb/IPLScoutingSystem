# Generated by Django 3.1.4 on 2020-12-13 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IPLAPP', '0007_scouting_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='odistat',
            name='id',
        ),
        migrations.RemoveField(
            model_name='t20stat',
            name='id',
        ),
        migrations.RemoveField(
            model_name='teststat',
            name='id',
        ),
        migrations.AlterField(
            model_name='odistat',
            name='odi_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='IPLAPP.player'),
        ),
        migrations.AlterField(
            model_name='t20stat',
            name='t20_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='IPLAPP.player'),
        ),
        migrations.AlterField(
            model_name='teststat',
            name='test_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='IPLAPP.player'),
        ),
    ]
