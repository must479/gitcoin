# Generated by Django 2.2.24 on 2021-10-29 17:48

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0193_tip_value_in_usdt'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='searchhistory',
            options={'verbose_name_plural': 'Bounties'},
        ),
        migrations.AlterField(
            model_name='searchhistory',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(db_index=True, default=dict),
        ),
        migrations.AlterField(
            model_name='searchhistory',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterIndexTogether(
            name='searchhistory',
            index_together={('data', 'search_type', 'ip_address'), ('data', 'search_type', 'ip_address', 'user')},
        ),
    ]
