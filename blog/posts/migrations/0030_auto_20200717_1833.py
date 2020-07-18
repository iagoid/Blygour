# Generated by Django 3.0.8 on 2020-07-17 21:33

from django.db import migrations
import django_fields.fields
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0029_auto_20200717_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=django_fields.fields.DefaultStaticImageField(blank=True, null=True, upload_to=posts.models.get_file_path, verbose_name='Imagem'),
        ),
    ]