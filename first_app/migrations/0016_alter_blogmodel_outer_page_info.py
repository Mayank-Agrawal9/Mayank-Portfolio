# Generated by Django 4.1.5 on 2023-03-11 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0015_homepage_meta_description_homepage_meta_keyword_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='outer_page_info',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
