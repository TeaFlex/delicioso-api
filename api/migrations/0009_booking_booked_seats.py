# Generated by Django 3.2.12 on 2022-02-24 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20220222_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booked_seats',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]