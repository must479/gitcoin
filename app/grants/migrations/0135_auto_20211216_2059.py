# Generated by Django 2.2.24 on 2021-12-16 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0134_merge_20211216_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='clrmatch',
            name='claim_tx',
            field=models.CharField(blank=True, help_text='The claim txid', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='grantpayout',
            name='network',
            field=models.CharField(choices=[('mainnet', 'mainnet'), ('rinkeby', 'rinkeby')], default='mainnet', help_text='Network where contract is deployed', max_length=15),
        ),
        migrations.AlterField(
            model_name='clrmatch',
            name='payout_tx',
            field=models.CharField(blank=True, help_text='The payout txid', max_length=255),
        ),
    ]
