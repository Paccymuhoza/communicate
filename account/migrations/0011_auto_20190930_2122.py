# Generated by Django 2.2.5 on 2019-09-30 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20190930_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='name',
            field=models.CharField(max_length=5),
        ),
    ]
