# Generated by Django 4.0.6 on 2022-07-13 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='YouTubeSearcher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Searcher_Email', models.EmailField(max_length=254)),
            ],
        ),
    ]