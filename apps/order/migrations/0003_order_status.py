# Generated by Django 3.2 on 2021-11-06 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20211030_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, default='Order Placed', max_length=255, null=True),
        ),
    ]
