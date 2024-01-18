from django.contrib import admin

from api.models import News, Category
from modeltranslation.admin import TranslationAdmin


class NewsAdmin(TranslationAdmin):
    pass


class CategoryAdmin(TranslationAdmin):
    pass


# Register your models here.
admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
