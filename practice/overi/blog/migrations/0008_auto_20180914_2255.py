# Generated by Django 2.1 on 2018-09-14 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20180914_2251'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='date',
            new_name='date1',
        ),
    ]
