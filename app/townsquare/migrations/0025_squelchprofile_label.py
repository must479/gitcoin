# Generated by Django 2.2.24 on 2021-09-16 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('townsquare', '0024_auto_20201007_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='squelchprofile',
            name='label',
            field=models.CharField(choices=[('Human', 'Human'), ('Heuristic', 'Heuristic'), ('Prediction', 'Prediction')], default='Human', help_text='means used to mark user as sybil', max_length=20),
        ),
    ]
