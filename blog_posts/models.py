from typing import Text
from django.db import models
from django.db.models.deletion import CASCADE, RESTRICT, SET_NULL
from django.db.models.fields import BooleanField, CharField, DateField, EmailField, SlugField, TextField
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.db.models.fields.files import ImageField


# Create your models here.

class tag(models.Model):
    caption = CharField(max_length=50)

    def __str__(self):
        return self.caption


    def __str__(self):
        return f"{self.title}-{self.author}-{self.date}"



class user(models.Model):
    name = CharField(max_length=40,unique=True)
    password = CharField(max_length=30)
    email = EmailField(unique=True)
    readLater = models.JSONField(null = True)
    code = CharField(max_length=15,db_index=True)
    isSuperUser = BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.email}"

class post(models.Model):
    title = models.CharField(max_length=50)
    clickbait = models.CharField(max_length=200,null=True)
    content = models.TextField()
    date = DateField()
    author = ForeignKey(user,on_delete=SET_NULL,null=True)
    tags = ManyToManyField(tag)
    slug = SlugField(null=True,unique=True,db_index=True)
    image = ImageField(upload_to = "data")

class comment(models.Model):
    name = CharField(max_length=50)
    content = TextField()
    post = ForeignKey(post, on_delete=CASCADE, null=True)

    def __str__(self):
        return f'{self.name} - {self.post}'




