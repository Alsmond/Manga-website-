# Generated by Django 4.2a1 on 2023-02-13 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=50)),
                ('bio', models.TextField()),
            ],
        ),
    ]
