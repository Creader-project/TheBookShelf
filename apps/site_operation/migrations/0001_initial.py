# Generated by Django 3.2.10 on 2021-12-30 21:23

from django.db import migrations, models
import django.db.models.deletion
import site_operation.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bookitem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promotion', models.CharField(default='', max_length=1000, verbose_name='promotion')),
                ('activation', models.CharField(choices=[('Inactive', 'Inactive'), ('Active', 'Active')], default='Inactive', max_length=1000, verbose_name='Publish status')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_page', to='bookitem.book', verbose_name='book')),
            ],
        ),
        migrations.CreateModel(
            name='IndexImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(default='', max_length=1000, verbose_name='alt text')),
                ('book_image', models.ImageField(default='media/image/default.png', max_length=1000, upload_to=site_operation.models.image_upload_path, verbose_name='Book image')),
                ('activation', models.CharField(choices=[('Inactive', 'Inactive'), ('Active', 'Active')], default='Inactive', max_length=1000, verbose_name='Publish status')),
                ('book', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='index_book_image', to='bookitem.book', verbose_name='book')),
            ],
        ),
    ]
