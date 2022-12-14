# Generated by Django 2.2.24 on 2021-10-02 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kudos', '0020_auto_20210924_0616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='hidden',
            field=models.BooleanField(db_index=True, default=False, help_text='Hide from marketplace?'),
        ),
        migrations.AlterField(
            model_name='token',
            name='num_clones_allowed',
            field=models.IntegerField(blank=True, db_index=True, null=True),
        ),
    ]
