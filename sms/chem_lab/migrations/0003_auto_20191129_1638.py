# Generated by Django 2.2.7 on 2019-11-29 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chem_lab', '0002_auto_20191127_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chem_con',
            name='chem_amount',
            field=models.FloatField(),
        ),
    ]