# Generated by Django 2.0.7 on 2018-07-30 07:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('salary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='salarylist',
            name='user',
            field=models.ForeignKey(help_text='姓名', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='姓名'),
        ),
        migrations.AddField(
            model_name='salary',
            name='user',
            field=models.ForeignKey(help_text='员工', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='员工'),
        ),
    ]
