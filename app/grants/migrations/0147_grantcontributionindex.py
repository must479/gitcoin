# Generated by Django 2.2.24 on 2022-08-16 12:10

from django.db import migrations, models
import django.db.models.deletion
import economy.models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0210_auto_20220718_1306'),
        ('grants', '0146_auto_20220809_1134'),
    ]

    operations = [
        migrations.CreateModel(
            name='GrantContributionIndex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('round_num', models.IntegerField(help_text='The round number a user contributed to')),
                ('grant', models.ForeignKey(help_text='The grant a user contributed to', on_delete=django.db.models.deletion.CASCADE, to='grants.Grant')),
                ('profile', models.ForeignKey(help_text='Contributor', on_delete=django.db.models.deletion.CASCADE, to='dashboard.Profile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
