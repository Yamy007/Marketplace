# Generated by Django 5.1.7 on 2025-03-14 16:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MarketPlaceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
                ('description', models.CharField(max_length=255)),
                ('slogan', models.CharField(max_length=25)),
                ('image', models.ImageField(blank=True, null=True, upload_to='marketplace/')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='marketplace', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'marketplace',
            },
        ),
    ]
