# Generated by Django 2.2.7 on 2019-11-27 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chem_lab', '0002_auto_20191127_1342'),
        ('bio_lab', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bio_broken_eq',
            fields=[
                ('bio_eq_id', models.IntegerField(primary_key=True, serialize=False)),
                ('bio_eq_name', models.CharField(max_length=50)),
                ('bio_eq_number', models.IntegerField()),
                ('bio_eq_cost', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chem_lab.student', verbose_name='student')),
            ],
        ),
        migrations.CreateModel(
            name='bio_eq',
            fields=[
                ('bio_eq_id', models.IntegerField(primary_key=True, serialize=False)),
                ('bio_eq_name', models.CharField(max_length=50)),
                ('bio_eq_amount', models.PositiveIntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='chem',
        ),
    ]
