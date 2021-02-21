# Generated by Django 3.1.5 on 2021-02-21 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210221_1641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(default='a@c.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default='name', max_length=80),
            preserve_default=False,
        ),
    ]