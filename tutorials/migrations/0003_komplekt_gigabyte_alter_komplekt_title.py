# Generated by Django 4.0.1 on 2022-01-16 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0002_komplekt_delete_tutorial'),
    ]

    operations = [
        migrations.AddField(
            model_name='komplekt',
            name='gigabyte',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='komplekt',
            name='title',
            field=models.CharField(default='', max_length=140),
        ),
    ]
