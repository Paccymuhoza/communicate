# Generated by Django 2.2.5 on 2019-10-22 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_auto_20191022_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='category',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='student',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
