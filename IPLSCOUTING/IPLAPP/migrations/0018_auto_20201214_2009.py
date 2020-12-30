# Generated by Django 3.1.4 on 2020-12-14 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IPLAPP', '0017_auto_20201214_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='odistat',
            name='odi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='IPLAPP.player'),
        ),
        migrations.AlterField(
            model_name='t20stat',
            name='t20',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='IPLAPP.player'),
        ),
        migrations.AlterField(
            model_name='teststat',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='IPLAPP.player'),
        ),
    ]
