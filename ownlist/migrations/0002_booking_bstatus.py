# Generated by Django 3.1.6 on 2021-08-19 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ownlist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='bstatus',
            field=models.TextField(default=''),
        ),
    ]
