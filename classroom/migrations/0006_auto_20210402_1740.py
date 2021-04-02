# Generated by Django 3.0.4 on 2021-04-02 16:40

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0005_auto_20210402_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='Passage',
            field=tinymce.models.HTMLField(default='None'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='instructions',
            field=tinymce.models.HTMLField(default='none'),
            preserve_default=False,
        ),
    ]
