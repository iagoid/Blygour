# Generated by Django 3.0.8 on 2020-07-17 21:23

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0027_auto_20200717_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='profiles/avatar.png', upload_to=posts.models.get_file_path, verbose_name='Imagem'),
        ),
    ]
