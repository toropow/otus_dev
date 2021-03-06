# Generated by Django 3.1.3 on 2020-11-28 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('is_man', models.BooleanField(default=True)),
                ('about', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PublishingHouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('address', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_book', models.TextField(blank=True)),
                ('rating', models.PositiveSmallIntegerField(default=0)),
                ('author_review', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='library.author')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('release', models.DateField()),
                ('isbn', models.IntegerField()),
                ('name_book', models.CharField(max_length=256)),
                ('author', models.ManyToManyField(to='library.Author')),
                ('publishing_house', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='library.publishinghouse')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.review')),
            ],
        ),
    ]
