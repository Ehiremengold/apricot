# Generated by Django 3.2 on 2022-02-15 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_dashboard_wallet_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard',
            name='wallet_tag',
            field=models.CharField(default='qEGlLbjidqAzRn5y', max_length=16, unique=True),
        ),
    ]
