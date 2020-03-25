# Generated by Django 2.2 on 2020-03-24 17:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='cp',
            field=models.ImageField(upload_to='pics/stores'),
        ),
        migrations.AlterField(
            model_name='store',
            name='dp',
            field=models.ImageField(upload_to='pics/stores'),
        ),
        migrations.AlterField(
            model_name='store',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
