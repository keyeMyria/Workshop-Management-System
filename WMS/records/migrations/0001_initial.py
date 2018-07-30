# Generated by Django 2.0.7 on 2018-07-30 07:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecordIron',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_number', models.IntegerField(default=0, help_text='状态 / 已经入库数量', verbose_name='状态 / 已经入库数量')),
                ('number', models.IntegerField(help_text='数量', verbose_name='数量')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, help_text='时间', verbose_name='时间')),
                ('updated_datetime', models.DateTimeField(auto_now=True, help_text='最后修改时间', verbose_name='最后修改时间')),
            ],
            options={
                'verbose_name': '熨烫记工',
                'verbose_name_plural': '熨烫记工',
                'db_table': 'records_iron',
            },
        ),
        migrations.CreateModel(
            name='RecordOutput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_number', models.IntegerField(default=0, help_text='状态 / 已经入库数量', verbose_name='状态 / 已经入库数量')),
                ('number', models.IntegerField(help_text='数量', verbose_name='数量')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, help_text='时间', verbose_name='时间')),
                ('updated_datetime', models.DateTimeField(auto_now=True, help_text='最后修改时间', verbose_name='最后修改时间')),
            ],
            options={
                'verbose_name': '出库记录',
                'verbose_name_plural': '出库记录',
                'db_table': 'records_output',
            },
        ),
        migrations.CreateModel(
            name='RecordSew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_number', models.IntegerField(default=0, help_text='状态 / 已经入库数量', verbose_name='状态 / 已经入库数量')),
                ('number', models.IntegerField(help_text='数量', verbose_name='数量')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, help_text='时间', verbose_name='时间')),
                ('updated_datetime', models.DateTimeField(auto_now=True, help_text='最后修改时间', verbose_name='最后修改时间')),
            ],
            options={
                'verbose_name': '缝纫记工',
                'verbose_name_plural': '缝纫记工',
                'db_table': 'records_sew',
            },
        ),
        migrations.CreateModel(
            name='RecordTailor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_number', models.IntegerField(default=0, help_text='上次记录', verbose_name='上次记录')),
                ('number', models.IntegerField(help_text='数量', verbose_name='数量')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, help_text='时间', verbose_name='时间')),
                ('updated_datetime', models.DateTimeField(auto_now=True, help_text='最后修改时间', verbose_name='最后修改时间')),
                ('product', models.ForeignKey(help_text='产品', on_delete=django.db.models.deletion.CASCADE, to='products.Product', verbose_name='产品')),
            ],
            options={
                'verbose_name': '裁剪记工',
                'verbose_name_plural': '裁剪记工',
                'db_table': 'records_tailor',
            },
        ),
    ]
