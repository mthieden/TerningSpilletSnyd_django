# Generated by Django 2.1.7 on 2019-03-25 08:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20190319_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='players',
            field=models.PositiveIntegerField(default=2, validators=[django.core.validators.MinValueValidator(2), django.core.validators.MaxValueValidator(6)]),
        ),
    ]
