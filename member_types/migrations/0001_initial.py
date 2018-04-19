# Generated by Django 2.0.3 on 2018-04-18 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MemberType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('monthly_fee', models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('registration_fee', models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)),
            ],
        ),
    ]