# Generated by Django 4.0 on 2022-01-05 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_delete_register'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
