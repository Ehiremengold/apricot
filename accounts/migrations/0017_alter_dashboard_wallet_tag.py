# Generated by Django 3.2 on 2022-02-16 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_alter_dashboard_wallet_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard',
            name='wallet_tag',
            field=models.CharField(default='sltmx0k0qqmqxurb', max_length=16, unique=True),
        ),
    ]
