# Generated by Django 4.0.2 on 2022-05-29 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mnft',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
