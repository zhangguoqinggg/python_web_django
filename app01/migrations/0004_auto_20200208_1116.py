# Generated by Django 2.2.5 on 2020-02-08 03:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='publisher_id',
            new_name='publisher',
        ),
    ]
