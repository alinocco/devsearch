# Generated by Django 4.0.5 on 2022-06-15 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_owner_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='users/user-default.png', null=True, upload_to='users/'),
        ),
    ]
