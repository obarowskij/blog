# Generated by Django 3.2.4 on 2021-10-17 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_posts', '0015_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='isSuperUser',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='code',
            field=models.CharField(db_index=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]
