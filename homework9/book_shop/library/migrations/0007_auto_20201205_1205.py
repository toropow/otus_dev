# Generated by Django 3.1.3 on 2020-12-05 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_book_photo_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='photo_book',
            new_name='image',
        ),
    ]
