# Generated by Django 2.1.7 on 2019-03-12 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjektRPGtekstowy', '0006_auto_20190312_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(),
        ),
    ]