# Generated by Django 3.0 on 2022-05-11 02:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('PortfoliosAPP', '0005_auto_20220510_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='technologie',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
