# Generated by Django 2.2.8 on 2019-12-25 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chem_lab', '0007_remove_ch_broken_eq_chem_eq_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='chem_con',
            name='reo',
            field=models.PositiveIntegerField(default=500),
            preserve_default=False,
        ),
    ]