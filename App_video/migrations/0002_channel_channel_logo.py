# Generated by Django 4.2.2 on 2023-06-20 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_video', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='channel_logo',
            field=models.ImageField(default=0.10869565217391304, upload_to='channel_logo'),
            preserve_default=False,
        ),
    ]
