# Generated by Django 2.0.7 on 2018-07-28 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20180728_2202'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='yt_price',
            new_name='iron_price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='bz_price',
            new_name='packag_price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='fr_price',
            new_name='sew_price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='cj_price',
            new_name='tailor_price',
        ),
    ]