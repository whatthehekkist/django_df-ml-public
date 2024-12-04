# Generated by Django 4.2.16 on 2024-10-14 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.IntegerField()),
                ('title', models.CharField(max_length=300)),
                ('genre', models.CharField(max_length=1000)),
                ('movie_image', models.ImageField(blank=True, null=True, upload_to='recommend/thumbnails', verbose_name='영화 이미지')),
            ],
        ),
    ]
