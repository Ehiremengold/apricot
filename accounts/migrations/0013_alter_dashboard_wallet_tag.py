# Generated by Django 3.2 on 2022-02-16 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_dashboard_wallet_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard',
            name='wallet_tag',
            field=models.CharField(default='r2e4sc63zbq9r94l', max_length=16, unique=True),
        ),
    ]