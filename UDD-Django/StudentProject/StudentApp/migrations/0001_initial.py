# Generated by Django 4.1 on 2022-10-16 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('ID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=12)),
                ('std', models.CharField(max_length=122)),
                ('sec', models.CharField(max_length=122)),
                ('roll', models.CharField(max_length=122)),
            ],
        ),
    ]
