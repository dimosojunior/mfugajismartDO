# Generated by Django 4.2.6 on 2025-01-17 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0026_remove_watejawote2_is_red_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='watejawote',
            name='IdadiYaJumla',
            field=models.IntegerField(blank=True, default=1, null=True, verbose_name='Idadi'),
        ),
        migrations.AddField(
            model_name='watejawote',
            name='Kiasi_Au_Idadi',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Unit'),
        ),
    ]
