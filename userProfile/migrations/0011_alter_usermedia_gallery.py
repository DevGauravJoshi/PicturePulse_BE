# Generated by Django 4.1.3 on 2022-11-08 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0010_alter_userinfo_usermedia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermedia',
            name='gallery',
            field=models.FileField(upload_to='gallery'),
        ),
    ]
