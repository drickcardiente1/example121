# Generated by Django 4.1.6 on 2023-02-17 05:50

from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
            ],
            options={
                'verbose_name': 'Renters',
                'verbose_name_plural': 'Renters',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('api.user',),
        ),
    ]
