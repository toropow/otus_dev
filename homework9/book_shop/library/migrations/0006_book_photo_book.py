# Generated by Django 3.1.3 on 2020-12-05 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_auto_20201205_0929'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='photo_book',
            field=models.ImageField(blank=True, null=True, upload_to='book'),
        ),
    ]
