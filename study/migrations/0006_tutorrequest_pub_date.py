# Generated by Django 3.0.3 on 2020-03-29 22:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0005_auto_20200324_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorrequest',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 29, 22, 22, 54, 261671, tzinfo=utc), verbose_name='date published'),
            preserve_default=False,
        ),
    ]
