# Generated by Django 2.2.7 on 2019-11-30 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chem_lab', '0005_delete_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ch_broken_eq',
            name='chem_eq_cost',
        ),
        migrations.AddField(
            model_name='chem_eq',
            name='chem_eq_cost',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]