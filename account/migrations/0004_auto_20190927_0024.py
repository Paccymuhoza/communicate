# Generated by Django 2.2.5 on 2019-09-26 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20190927_0004'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='academic_council',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='myuser',
            name='category',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='myuser',
            name='college_council',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='myuser',
            name='department',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='myuser',
            name='department_council',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='myuser',
            name='lecturer',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='myuser',
            name='level',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='myuser',
            name='phone',
            field=models.IntegerField(blank=True, default=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='regNo',
            field=models.IntegerField(blank=True, default=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='school',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='myuser',
            name='school_council',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='myuser',
            name='staffId',
            field=models.IntegerField(blank=True, default=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='student',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
