# Generated by Django 3.1.2 on 2020-10-17 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('address', models.TextField(max_length=300)),
                ('state', models.CharField(max_length=50, unique=True)),
                ('mobile_number', models.CharField(max_length=12)),
                ('email', models.EmailField(blank=True, default='', max_length=254)),
                ('bank_name', models.CharField(blank=True, default='', max_length=50)),
                ('bank_branch_address', models.TextField(blank=True, default='', max_length=300)),
                ('bank_ac_number', models.CharField(blank=True, default='', max_length=30)),
                ('bank_ifsc_code', models.CharField(blank=True, default='', max_length=30)),
                ('gstin_number', models.CharField(blank=True, default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaxSlab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
            ],
        ),
    ]