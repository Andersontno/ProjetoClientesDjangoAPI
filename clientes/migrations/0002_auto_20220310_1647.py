# Generated by Django 3.0.8 on 2022-03-10 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
