# Generated by Django 2.2.7 on 2019-11-29 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio_lab', '0002_auto_20191127_1342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bio_broken_eq',
            name='bio_eq_cost',
        ),
        migrations.RemoveField(
            model_name='bio_broken_eq',
            name='bio_eq_number',
        ),
        migrations.RemoveField(
            model_name='bio_broken_eq',
            name='student',
        ),
        migrations.AddField(
            model_name='bio_broken_eq',
            name='student_id',
            field=models.PositiveIntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bio_eq',
            name='bio_eq_cost',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]