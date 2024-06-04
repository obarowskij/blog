# Generated by Django 3.2.4 on 2021-10-17 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_posts', '0019_auto_20211017_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog_posts.user'),
        ),
        migrations.RemoveField(
            model_name='user',
            name='readLater',
        ),
        migrations.AddField(
            model_name='user',
            name='readLater',
            field=models.JSONField(null=True),
        ),
    ]