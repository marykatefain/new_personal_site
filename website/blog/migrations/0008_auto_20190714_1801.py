# Generated by Django 2.2.1 on 2019-07-14 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_blogpostpage_external_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpostpage',
            name='external_link',
            field=models.URLField(blank=True, help_text='Link to the original source', null=True),
        ),
    ]