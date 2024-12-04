# Generated by Django 4.2.16 on 2024-09-25 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_user_options_remove_user_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='account/profile', verbose_name='프로필 이미지'),
        ),
        migrations.AddField(
            model_name='user',
            name='short_description',
            field=models.TextField(blank=True, verbose_name='소개글'),
        ),
    ]
