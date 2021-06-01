# Generated by Django 3.1.6 on 2021-06-01 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ownlist', '0002_auto_20210503_1007'),
    ]

    operations = [
        migrations.CreateModel(
            name='CATEGORY',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ecategory', models.TextField(default='')),
                ('eplaces', models.TextField(default='')),
                ('eaddress', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='PERSONAL_INFORMATION',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tname', models.TextField(default='')),
                ('taddress', models.TextField(default='')),
                ('tnumber', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='REVIEWS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ereviews', models.TextField(default='')),
                ('edate', models.TextField(default='')),
                ('eexpenses', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='STATUS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ecomments', models.TextField(default='')),
                ('efeedback', models.TextField(default='')),
                ('reviews', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ownlist.reviews')),
            ],
        ),
        migrations.CreateModel(
            name='TRAVEL_DETAILS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etravelTips', models.TextField(default='')),
                ('etraveldetails', models.TextField(default='')),
                ('category', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ownlist.category')),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='List',
        ),
        migrations.AddField(
            model_name='reviews',
            name='travel_details',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ownlist.travel_details'),
        ),
        migrations.AddField(
            model_name='category',
            name='personal_information',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ownlist.personal_information'),
        ),
    ]
