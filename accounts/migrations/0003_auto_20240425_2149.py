# Generated by Django 3.2.14 on 2024-04-25 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_emailtemplate'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='exp_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='otp',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
