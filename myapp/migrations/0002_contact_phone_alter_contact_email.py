# Generated by Django 4.0.6 on 2022-07-06 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
