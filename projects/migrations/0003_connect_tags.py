# Generated by Django 4.0.5 on 2022-06-10 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_tags_and_reviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='projects.tag'),
        ),
        migrations.AddField(
            model_name='project',
            name='vote_ratio',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='vote_total',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]