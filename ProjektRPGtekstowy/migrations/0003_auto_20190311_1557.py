# Generated by Django 2.1.7 on 2019-03-11 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjektRPGtekstowy', '0002_remove_random_zdazenie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='hp',
            field=models.IntegerField(default=15),
        ),
        migrations.AlterField(
            model_name='player',
            name='hpp',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='int',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='player',
            name='sil',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='player',
            name='szc',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='player',
            name='zre',
            field=models.IntegerField(default=1),
        ),
    ]
