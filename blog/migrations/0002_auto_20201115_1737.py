# Generated by Django 3.1.3 on 2020-11-15 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category'},
        ),
        migrations.AlterModelTable(
            name='category',
            table='state',
        ),
    ]
