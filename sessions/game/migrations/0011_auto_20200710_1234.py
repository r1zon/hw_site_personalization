# Generated by Django 3.0.7 on 2020-07-10 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0010_playergameinfo_try_counts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playergameinfo',
            name='try_counts',
            field=models.IntegerField(default=0),
        ),
    ]
