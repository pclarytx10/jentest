# Generated by Django 4.1.7 on 2023-02-17 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0003_alter_coin_last_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
