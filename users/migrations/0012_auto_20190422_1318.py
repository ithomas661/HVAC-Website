# Generated by Django 2.1 on 2019-04-22 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20190422_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.Profile'),
        ),
    ]