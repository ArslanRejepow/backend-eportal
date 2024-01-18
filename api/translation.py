from modeltranslation.translator import translator, TranslationOptions
from .models import News, Category


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
    required_languages = []


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)
    required_languages = []


translator.register(News, NewsTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
