# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-19 21:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registrant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Dr.', 'dr.'), ('Mr.', 'mr.'), ('Ms.', 'ms.'), ('Mrs.', 'mrs.')], max_length=5)),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=25)),
                ('date_of_registration', models.DateField(auto_now_add=True)),
                ('street_address_1', models.CharField(max_length=30)),
                ('street_address_2', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=2)),
                ('zipcode', models.CharField(max_length=10)),
                ('telephone', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=30)),
                ('website', models.URLField(max_length=100)),
                ('position', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=50)),
                ('meals', models.CharField(choices=[('mealpack', 'mealpack'), ('dinnerday2', 'dinnerday2')], max_length=15)),
                ('billing_firstname', models.CharField(max_length=20)),
                ('billing_lastname', models.CharField(max_length=25)),
                ('card_type', models.CharField(choices=[('V', 'Visa'), ('MC', 'Mastercard'), ('AE', 'American Express')], max_length=30)),
                ('card_number', models.CharField(max_length=16)),
                ('card_csv', models.CharField(max_length=4)),
                ('exp_year', models.CharField(max_length=4)),
                ('exp_month', models.CharField(max_length=2)),
                ('session1', models.CharField(choices=[('Workshop A', 'Workshop A'), ('Workshop B', 'Workshop B'), ('Workshop C', 'Workshop C')], max_length=15)),
                ('session2', models.CharField(choices=[('Workshop D', 'Workshop D'), ('Workshop E', 'Workshop E'), ('Workshop F', 'Workshop F')], max_length=15)),
                ('session3', models.CharField(choices=[('Workshop G', 'Workshop G'), ('Workshop H', 'Workshop H'), ('Workshop I', 'Workshop I')], max_length=15)),
            ],
        ),
    ]
