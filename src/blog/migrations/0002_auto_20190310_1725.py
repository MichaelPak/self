# Generated by Django 2.1 on 2019-03-10 17:25

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='intro',
            field=wagtail.core.fields.RichTextField(),
        ),
    ]
