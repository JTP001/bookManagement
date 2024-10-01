# Generated by Django 5.1.1 on 2024-09-28 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entryID', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=50)),
                ('pubDate', models.DateField()),
                ('isbn', models.CharField(max_length=17)),
            ],
        ),
    ]
