# Generated by Django 2.2.6 on 2019-10-31 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_auto_20191022_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='regNo',
            field=models.CharField(max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='staffId',
            field=models.CharField(max_length=9, null=True),
        ),
    ]
