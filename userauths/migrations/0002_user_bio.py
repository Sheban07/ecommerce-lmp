# Generated by Django 3.2.25 on 2024-11-29 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
