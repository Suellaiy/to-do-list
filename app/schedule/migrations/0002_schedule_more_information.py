# Generated by Django 2.2.9 on 2020-01-31 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='more_information',
            field=models.TextField(max_length=300, null=True),
        ),
    ]