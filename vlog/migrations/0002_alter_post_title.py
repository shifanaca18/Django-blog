# Generated by Django 4.1 on 2023-01-02 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vlog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]