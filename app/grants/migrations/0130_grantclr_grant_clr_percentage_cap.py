# Generated by Django 2.2.24 on 2021-11-24 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0129_auto_20211116_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='grantclr',
            name='grant_clr_percentage_cap',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Percentage of total pot at which Grant CLR should be capped', max_digits=6, null=True),
        ),
    ]