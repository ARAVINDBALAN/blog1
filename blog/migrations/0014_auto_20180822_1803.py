# Generated by Django 2.1 on 2018-08-22 18:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20180822_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_like',
            field=models.ManyToManyField(related_name='post_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
