# Generated by Django 2.1.5 on 2019-01-09 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='body',
            field=models.CharField(default='Type content here', max_length=500),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
