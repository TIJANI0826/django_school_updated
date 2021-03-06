# Generated by Django 3.0.4 on 2021-04-02 16:47

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0006_auto_20210402_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='Passage',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='instructions',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='Passage',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='instructions',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]
