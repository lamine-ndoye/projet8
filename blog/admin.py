from django.contrib import admin
from .models import Category,article
# Register your models here.


admin.site.register(Category)


@admin.register(article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titel','image','description','create','update','publish','autors')
    prepopulated = {'details':('titel',)}
    search_fields = ('titel','description')
    ordering = ('autors','image','publish')
    list_filter = ('autors','create','publish')


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name','slug')
