# Generated by Django 2.2.9 on 2022-05-31 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userprofile_last_2fa_attempt'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='timeout_for_2fa',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
