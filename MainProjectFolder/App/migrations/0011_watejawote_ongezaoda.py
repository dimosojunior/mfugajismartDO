# Generated by Django 4.2.6 on 2024-10-08 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0010_watejawote_day_is_reached_watejawote_message_is_sent'),
    ]

    operations = [
        migrations.AddField(
            model_name='watejawote',
            name='OngezaOda',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Peleka Oda Mbele Kwa Siku ?'),
        ),
    ]
