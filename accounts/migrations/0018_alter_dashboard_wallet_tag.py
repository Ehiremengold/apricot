# Generated by Django 3.2 on 2022-02-16 21:24

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_alter_dashboard_wallet_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard',
            name='wallet_tag',
            field=models.CharField(default=accounts.models.unique_rand, max_length=16, unique=True),
        ),
    ]
