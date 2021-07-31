# Generated by Django 3.1.3 on 2020-12-04 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discuss',
            name='email',
            field=models.EmailField(max_length=264, unique=True),
        ),
        migrations.AlterField(
            model_name='discuss',
            name='message',
            field=models.CharField(max_length=64000),
        ),
    ]
