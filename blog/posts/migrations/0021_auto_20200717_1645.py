# Generated by Django 3.0.8 on 2020-07-17 19:45

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0020_delete_commentsanswer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, default='profiles/avatar.png', null=True, upload_to=posts.models.get_file_path, verbose_name='Imagem'),
        ),
    ]
