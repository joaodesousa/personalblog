# Generated by Django 3.0.4 on 2020-03-16 12:18

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200315_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='byline',
            field=models.CharField(max_length=275, verbose_name='Subtítulo'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=ckeditor.fields.RichTextField(verbose_name='Corpo'),
        ),
    ]
