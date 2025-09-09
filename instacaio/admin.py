from django.contrib import admin

from instacaio import models

# Register your models here.
@admin.register(models.Post)
class AdminPost(admin.ModelAdmin):
    pass