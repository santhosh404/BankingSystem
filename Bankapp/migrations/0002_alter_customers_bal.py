# Generated by Django 3.2 on 2021-08-11 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bankapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='bal',
            field=models.IntegerField(),
        ),
    ]
