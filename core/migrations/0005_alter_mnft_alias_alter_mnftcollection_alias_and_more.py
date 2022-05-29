# Generated by Django 4.0.2 on 2022-05-29 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_mnftcollection_symbol_blockchain_symbol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mnft',
            name='alias',
            field=models.CharField(blank=True, max_length=300, unique=True),
        ),
        migrations.AlterField(
            model_name='mnftcollection',
            name='alias',
            field=models.CharField(blank=True, max_length=300, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='alias',
            field=models.CharField(blank=True, max_length=300, unique=True),
        ),
    ]