# Generated by Django 4.1.7 on 2023-02-16 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coin_name', models.CharField(max_length=50)),
                ('api_id', models.CharField(blank=True, max_length=250)),
                ('coin_symbol', models.CharField(blank=True, max_length=10)),
                ('last_updated', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ('coin_name',),
            },
        ),
    ]
