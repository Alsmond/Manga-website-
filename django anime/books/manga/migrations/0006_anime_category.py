# Generated by Django 4.2a1 on 2023-02-13 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0005_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='category',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='manga.category'),
            preserve_default=False,
        ),
    ]
