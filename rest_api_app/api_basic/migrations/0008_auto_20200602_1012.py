# Generated by Django 3.0.6 on 2020-06-02 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0007_auto_20200602_1007'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='activityperiod',
            unique_together=set(),
        ),
    ]