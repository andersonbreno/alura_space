# Generated by Django 4.1.7 on 2023-02-24 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0005_alter_fotografia_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='publicada',
            field=models.BooleanField(default=False),
        ),
    ]
