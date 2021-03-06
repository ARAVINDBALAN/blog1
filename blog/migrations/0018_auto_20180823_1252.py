# Generated by Django 2.1 on 2018-08-23 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20180823_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='messages',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
