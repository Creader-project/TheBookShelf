# Generated by Django 3.2.10 on 2021-12-30 21:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookcase', '0002_bookmark_chapter'),
        ('bookitem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_marked', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='bookcase',
            name='book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bookitem.book', verbose_name='Book'),
        ),
        migrations.AddField(
            model_name='bookcase',
            name='bookmark',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='marked_book', to='bookcase.bookmark', verbose_name='bookmark'),
        ),
        migrations.AddField(
            model_name='bookcase',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User bookcase'),
        ),
    ]
