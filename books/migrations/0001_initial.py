# Generated by Django 4.2.4 on 2023-08-26 09:44

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
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('year', models.PositiveIntegerField()),
                ('publisher', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=255)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3)),
            ],
        ),
    ]
