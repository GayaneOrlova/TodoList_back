# Generated by Django 4.2.2 on 2023-07-03 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='code',
        ),
        migrations.AlterField(
            model_name='todo',
            name='checked',
            field=models.BooleanField(default=False, verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='value',
            field=models.CharField(blank=True, default='', max_length=500, verbose_name='todo point'),
        ),
    ]
