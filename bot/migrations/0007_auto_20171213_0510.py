# Generated by Django 2.0 on 2017-12-13 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0006_auto_20171211_0454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]