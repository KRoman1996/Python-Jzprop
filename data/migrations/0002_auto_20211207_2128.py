# Generated by Django 3.2.9 on 2021-12-07 13:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='criteria',
            name='active',
        ),
        migrations.AddField(
            model_name='complaint',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Timestamp'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='complaint',
            name='unique_key',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='Unique Key'),
        ),
        migrations.AlterField(
            model_name='criteria',
            name='name',
            field=models.CharField(blank=True, max_length=250, null=True, unique=True, verbose_name='Name'),
        ),
    ]
