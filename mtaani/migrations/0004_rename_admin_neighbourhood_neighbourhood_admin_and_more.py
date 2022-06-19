# Generated by Django 4.0.4 on 2022-06-18 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtaani', '0003_rename_post_by_business_post_post_business_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='neighbourhood',
            old_name='admin',
            new_name='neighbourhood_admin',
        ),
        migrations.RenameField(
            model_name='neighbourhood',
            old_name='description',
            new_name='neighbourhood_description',
        ),
        migrations.RenameField(
            model_name='neighbourhood',
            old_name='health_tell',
            new_name='neighbourhood_health_tell',
        ),
        migrations.RenameField(
            model_name='neighbourhood',
            old_name='hood_logo',
            new_name='neighbourhood_hood_logo',
        ),
        migrations.RenameField(
            model_name='neighbourhood',
            old_name='location',
            new_name='neighbourhood_location',
        ),
        migrations.RenameField(
            model_name='neighbourhood',
            old_name='name',
            new_name='neighbourhood_name',
        ),
        migrations.RenameField(
            model_name='neighbourhood',
            old_name='police_number',
            new_name='neighbourhood_police_number',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='name',
            new_name='profile_name',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='profile_user',
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]