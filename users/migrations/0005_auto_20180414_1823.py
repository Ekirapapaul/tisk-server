# Generated by Django 2.0.3 on 2018-04-14 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_national_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='national_id',
            field=models.CharField(blank=True, max_length=200, unique=True, verbose_name='national_id'),
        ),
    ]
