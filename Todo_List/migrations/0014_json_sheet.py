# Generated by Django 3.0.3 on 2020-06-03 19:48

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo_List', '0013_sheet_user_sheet'),
    ]

    operations = [
        migrations.CreateModel(
            name='JSON_sheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('json_title', models.CharField(default='JSON_Title', help_text='JSON', max_length=20, verbose_name='JSON')),
                ('json_file', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]
