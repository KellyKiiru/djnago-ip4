# Generated by Django 4.0.4 on 2022-06-21 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mtaani', '0003_alter_neighbourhood_neighbourhood_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_business',
        ),
    ]
