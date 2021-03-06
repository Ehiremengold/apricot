# Generated by Django 3.2 on 2022-02-08 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_dashboard_wallet_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard',
            name='wallet_balance',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=300),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='wallet_tag',
            field=models.CharField(default='puupwohB8C5J720C', max_length=16, unique=True),
        ),
    ]
