# Generated by Django 4.2.5 on 2023-09-26 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daybook', '0003_remove_daybook_profit'),
    ]

    operations = [
        migrations.AddField(
            model_name='daybook',
            name='num_of_customer',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='daybook',
            name='rival_info',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
    ]
