# Generated by Django 2.1 on 2019-03-13 19:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0008_auto_20190313_1229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='propertyID',
        ),
        migrations.AddField(
            model_name='property',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]