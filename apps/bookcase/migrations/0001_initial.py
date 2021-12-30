# Generated by Django 3.2.10 on 2021-12-30 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookcase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='Added time')),
            ],
            options={
                'verbose_name': 'Bookcase',
                'verbose_name_plural': 'Bookcase',
                'db_table': 'Bookcase',
            },
        ),
        migrations.CreateModel(
            name='BookMark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='added time')),
            ],
            options={
                'verbose_name': 'Bookmark',
                'db_table': 'Bookmark',
            },
        ),
    ]