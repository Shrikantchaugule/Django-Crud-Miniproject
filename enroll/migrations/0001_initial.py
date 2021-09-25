# Generated by Django 3.0.4 on 2021-09-25 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('roll', models.CharField(max_length=10)),
                ('branch', models.CharField(max_length=50)),
                ('year', models.IntegerField(max_length=1)),
                ('contact', models.IntegerField(max_length=10)),
            ],
        ),
    ]
