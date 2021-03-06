# Generated by Django 3.2 on 2022-04-21 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Department Name')),
                ('short_name', models.CharField(max_length=30, verbose_name='Department Acronym')),
            ],
            options={
                'verbose_name': 'Department',
                'verbose_name_plural': 'Departments',
            },
        ),
    ]
