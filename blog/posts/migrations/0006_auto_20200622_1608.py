# Generated by Django 3.0.7 on 2020-06-22 19:08

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20200616_1720'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['text'], 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=posts.models.get_file_path),
        ),
    ]
