# Generated by Django 2.2.24 on 2021-10-01 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0188_remove_profile_tribe_priority'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='portfolioitem',
            constraint=models.UniqueConstraint(fields=('profile', 'title', 'link'), name='unique_title_link_per_profile'),
        ),
    ]