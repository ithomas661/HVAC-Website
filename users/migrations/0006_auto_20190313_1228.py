# Generated by Django 2.1 on 2019-03-13 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190313_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='propertyID',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='users.Property'),
        ),
    ]
