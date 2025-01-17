# Generated by Django 3.2.10 on 2021-12-30 21:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('transactions', '0001_initial'),
        ('bookitem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction_history',
            name='to_user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='TO_USER', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='transaction_history',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='income_history',
            name='Author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='Author_ID', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='income_history',
            name='chapter',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Chapter_Income', to='bookitem.chapter', verbose_name='Chapter'),
        ),
        migrations.AddField(
            model_name='income_history',
            name='from_user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='Buyer_ID', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='income_history',
            name='transaction',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='transactions.transaction_history'),
        ),
        migrations.AddField(
            model_name='author_pool',
            name='Author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='Pool_User_ID', to=settings.AUTH_USER_MODEL),
        ),
    ]
