# Generated by Django 3.0 on 2022-05-11 02:06

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('PortfoliosAPP', '0002_auto_20220510_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='url',
            field=embed_video.fields.EmbedVideoField(),
        ),
    ]
