# Generated by Django 3.0.3 on 2020-06-02 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo_List', '0006_note_buffer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note_buffer',
            old_name='buf_titel',
            new_name='buf_title',
        ),
        migrations.RemoveField(
            model_name='note',
            name='note_titel',
        ),
        migrations.RemoveField(
            model_name='note',
            name='pub_date_n',
        ),
        migrations.AddField(
            model_name='note',
            name='dead_line',
            field=models.DateField(default=None, verbose_name='Dead Line'),
        ),
        migrations.AddField(
            model_name='note',
            name='note_title',
            field=models.CharField(default='Note_Title', help_text='Title', max_length=20, verbose_name='____Note Titlel'),
        ),
        migrations.AddField(
            model_name='note',
            name='real_date',
            field=models.DateField(default=None, verbose_name='Real date'),
        ),
        migrations.AddField(
            model_name='note',
            name='status',
            field=models.CharField(default='Not Performed', help_text='N_Status', max_length=20, verbose_name='status'),
        ),
        migrations.AddField(
            model_name='note_buffer',
            name='buf_dead_line',
            field=models.DateField(default=None, verbose_name='Dead Line'),
        ),
        migrations.AddField(
            model_name='note_buffer',
            name='buf_real_date',
            field=models.DateField(default=None, verbose_name='Real date'),
        ),
        migrations.AddField(
            model_name='note_buffer',
            name='buf_status',
            field=models.CharField(default='Not Performed', help_text='N_Status', max_length=20, verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='note',
            name='task_text',
            field=models.CharField(default='Task Text', help_text='Task', max_length=600, verbose_name='____Task Text'),
        ),
    ]
