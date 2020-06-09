# Generated by Django 3.0.3 on 2020-06-02 23:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Todo_List', '0007_auto_20200603_0234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='dead_line',
            field=models.DateField(default=datetime.datetime(2020, 6, 2, 23, 35, 53, 540997, tzinfo=utc), verbose_name='Dead Line'),
        ),
        migrations.AlterField(
            model_name='note',
            name='real_date',
            field=models.DateField(default=datetime.datetime(2020, 6, 2, 23, 35, 53, 540997, tzinfo=utc), verbose_name='Real date'),
        ),
        migrations.AlterField(
            model_name='note_buffer',
            name='buf_dead_line',
            field=models.DateField(default=datetime.datetime(2020, 6, 2, 23, 35, 53, 542026, tzinfo=utc), verbose_name='Dead Line'),
        ),
        migrations.AlterField(
            model_name='note_buffer',
            name='buf_real_date',
            field=models.DateField(default=datetime.datetime(2020, 6, 2, 23, 35, 53, 542026, tzinfo=utc), verbose_name='Real date'),
        ),
    ]
