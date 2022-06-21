# Generated by Django 4.0.4 on 2022-06-21 02:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mtaani', '0004_remove_post_post_business'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_profile',
        ),
        migrations.AlterField(
            model_name='post',
            name='post_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_owner', to='mtaani.profile'),
        ),
    ]
