# Generated by Django 3.2.3 on 2021-05-30 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='expires_on',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='poll',
            name='starts_on',
            field=models.DateField(auto_now_add=True),
        ),
    ]
