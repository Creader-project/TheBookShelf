# Generated by Django 3.2.7 on 2021-09-10 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0007_transaction_history_to_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='author_pool',
            name='Book_pool',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='author_pool',
            name='Chapter_Pool',
            field=models.IntegerField(default=0),
        ),
    ]
