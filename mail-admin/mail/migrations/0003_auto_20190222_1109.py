# Generated by Django 2.1.5 on 2019-02-21 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0002_auto_20190222_1107'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alias',
            options={'managed': False, 'verbose_name': 'Alias', 'verbose_name_plural': 'Aliases'},
        ),
        migrations.AlterModelOptions(
            name='domain',
            options={'managed': False, 'verbose_name': 'Domain', 'verbose_name_plural': 'Domains'},
        ),
        migrations.AlterModelOptions(
            name='email',
            options={'managed': False, 'verbose_name': 'Email', 'verbose_name_plural': 'Emails'},
        ),
    ]
