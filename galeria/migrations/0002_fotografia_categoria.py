# Generated by Django 4.1.7 on 2023-02-22 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='categoria',
            field=models.CharField(choices=[('NEBULOSA', 'nebulosa'), ('ESTRELA', 'estrela'), ('GALÁXIA', 'galáxia'), ('PLANETA', 'planeta')], default='', max_length=100),
        ),
    ]
