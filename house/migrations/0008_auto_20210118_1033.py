# Generated by Django 3.1.5 on 2021-01-18 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0007_auto_20210118_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
