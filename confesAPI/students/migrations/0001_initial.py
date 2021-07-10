# Generated by Django 3.2.5 on 2021-07-09 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('postId', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True)),
                ('StudentId', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('StudentId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=50)),
                ('profilePicName', models.CharField(max_length=100)),
            ],
        ),
    ]
