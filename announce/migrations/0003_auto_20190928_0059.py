# Generated by Django 2.2.5 on 2019-09-27 22:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('announce', '0002_auto_20190928_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announce',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='announces', to=settings.AUTH_USER_MODEL),
        ),
    ]
