# Generated by Django 3.2.4 on 2021-10-17 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_posts', '0016_auto_20211017_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]