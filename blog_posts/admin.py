from django.contrib import admin
from .models import post,tag,comment,user
# Register your models here.
class postAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author","tags","date")
    list_display = ("title","date","author")

admin.site.register(post,postAdmin)
admin.site.register(tag)
admin.site.register(comment)
admin.site.register(user)