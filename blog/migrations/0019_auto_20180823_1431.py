# Generated by Django 2.1 on 2018-08-23 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20180823_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(default='name', max_length=254, verbose_name='email'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='messages',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=200),
        ),
    ]