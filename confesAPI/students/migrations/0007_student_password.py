# Generated by Django 3.2.5 on 2021-07-09 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_alter_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(default='', max_length=100),
        ),
    ]
