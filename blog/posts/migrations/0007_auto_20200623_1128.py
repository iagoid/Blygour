# Generated by Django 3.0.7 on 2020-06-23 14:28

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20200622_1608'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['text'], 'verbose_name': 'Postagem', 'verbose_name_plural': 'Postagens'},
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default=1, max_length=120, verbose_name='Título'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Criado em :'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=posts.models.get_file_path, verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(verbose_name='Texto da Postagem'),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Modificado em :'),
        ),
    ]
