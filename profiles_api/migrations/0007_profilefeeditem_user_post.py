# Generated by Django 2.2 on 2021-02-11 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0006_remove_profilefeeditem_is_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilefeeditem',
            name='user_post',
            field=models.CharField(default='Hi', max_length=255),
        ),
    ]
