# Generated by Django 3.2 on 2023-01-19 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_plan_app', '0006_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='exp_date',
            field=models.DateField(null=True),
        ),
    ]
