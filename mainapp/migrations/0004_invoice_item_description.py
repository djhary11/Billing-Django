# Generated by Django 3.1.2 on 2020-10-26 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20201026_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='item_description',
            field=models.CharField(blank=True, default=' ', max_length=200),
        ),
    ]
