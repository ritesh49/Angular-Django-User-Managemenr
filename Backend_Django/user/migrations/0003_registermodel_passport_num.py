# Generated by Django 3.0.5 on 2020-07-24 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_registermodel_passport_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='registermodel',
            name='passport_num',
            field=models.CharField(default='0', max_length=12),
        ),
    ]