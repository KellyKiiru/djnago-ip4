# Generated by Django 4.0.4 on 2022-06-20 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mtaani', '0005_remove_profile_profile_email_profile_profile_tell_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_neighbourhood',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='members', to='mtaani.neighbourhood'),
        ),
    ]
