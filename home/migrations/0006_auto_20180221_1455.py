# Generated by Django 2.0.1 on 2018-02-21 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20180214_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.CharField(default='omar@gmail0com', max_length=30),
        ),
        migrations.AddField(
            model_name='contact',
            name='password',
            field=models.CharField(default=' ', max_length=30),
        ),
        migrations.AddField(
            model_name='contact',
            name='user_name',
            field=models.CharField(default='omar', max_length=30),
        ),
    ]
