# Generated by Django 4.0.5 on 2022-07-06 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_profile_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['created_date']},
        ),
    ]