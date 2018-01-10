# Generated by Django 2.0 on 2017-12-16 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0010_auto_20171215_0536'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Рассылка',
                'verbose_name': 'Рассылка',
            },
        ),
        migrations.AddField(
            model_name='settings',
            name='procent_fee',
            field=models.FloatField(blank=True, default=0.1, null=True),
        ),
        migrations.AddField(
            model_name='settings',
            name='wallet_for_fee',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
