# Generated by Django 3.2.10 on 2021-12-30 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=30, unique=True, verbose_name='Book title')),
                ('status', models.CharField(choices=[('Ongoing', 'Ongoing'), ('Completed', 'Completed')], default='Ongoing', max_length=150, null=True, verbose_name='Status')),
                ('short_description', models.TextField(default='', verbose_name='Short description')),
                ('description', models.TextField(default='', verbose_name='Book Description')),
                ('total_vote', models.IntegerField(default=0, editable=False, verbose_name='Total vote')),
                ('total_click', models.IntegerField(default=0, editable=False, verbose_name='Total Click')),
                ('fav_num', models.IntegerField(default=0, editable=False, verbose_name='Total favorite number')),
                ('added_time', models.DateTimeField(auto_now_add=True, verbose_name='Added time')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='last update')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
                'db_table': 'Book',
            },
        ),
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(default='', max_length=30, verbose_name='Category name')),
                ('category_code', models.CharField(default='', max_length=30, verbose_name='Category code')),
                ('is_tab', models.BooleanField(default=False, verbose_name='is Navigate')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='Added time')),
            ],
            options={
                'verbose_name': 'Type Category',
                'verbose_name_plural': 'Type categories',
                'db_table': 'Book Genre',
            },
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=150, verbose_name='Chapter title')),
                ('body', models.TextField(default='', verbose_name='Chapter text')),
                ('word_count', models.IntegerField(default=0, verbose_name='Word count')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Created time')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='last update')),
                ('publish_status', models.CharField(choices=[('Published', 'Published'), ('Draft', 'Draft'), ('Trash', 'Trash')], default='Published', max_length=150)),
                ('is_vip', models.BooleanField(default=False, verbose_name='VIP chapter')),
                ('coin_price', models.IntegerField(default=0)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chapter', to='bookitem.book', verbose_name='book')),
            ],
            options={
                'verbose_name': 'chapter',
                'verbose_name_plural': 'chapters',
                'db_table': 'Chapter',
            },
        ),
    ]
