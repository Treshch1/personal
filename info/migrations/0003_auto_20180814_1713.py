# Generated by Django 2.0.1 on 2018-08-14 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_auto_20180814_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='photo',
            field=models.ImageField(upload_to='uploaded_images'),
        ),
    ]