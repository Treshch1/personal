# Generated by Django 2.0.1 on 2018-10-22 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0007_auto_20181022_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='category',
            field=models.CharField(choices=[('sport', 'Sport'), ('it', 'IT')], default='it', max_length=10),
        ),
    ]
