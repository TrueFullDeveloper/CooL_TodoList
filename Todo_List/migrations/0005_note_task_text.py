# Generated by Django 3.0.3 on 2020-05-26 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo_List', '0004_auto_20200518_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='task_text',
            field=models.CharField(default='Task_Text', help_text='Task', max_length=600, verbose_name='____Task Text'),
        ),
    ]
