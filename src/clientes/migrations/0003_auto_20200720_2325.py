# Generated by Django 2.1.5 on 2020-07-21 04:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20200719_2325'),
    ]

    operations = [
        migrations.DeleteModel(
            name='cliente',
        ),
        migrations.DeleteModel(
            name='usuario',
        ),
    ]
