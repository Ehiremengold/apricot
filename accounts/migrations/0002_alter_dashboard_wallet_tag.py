# Generated by Django 4.0.1 on 2022-02-07 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard',
            name='wallet_tag',
            field=models.CharField(default='TOOknM1OrDV3P99q', max_length=16, unique=True),
        ),
    ]
