# Generated by Django 3.0.1 on 2020-01-24 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_mass_book_book_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='issues',
            name='book_name',
            field=models.CharField(default='temp', max_length=500),
            preserve_default=False,
        ),
    ]
