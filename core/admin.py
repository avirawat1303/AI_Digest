from django.contrib import admin
from .models import Article, Bookmark, UserPreferences, NewsletterLog

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title","category","date")
    list_filter = ("category","date")

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ("user","article","created_at")

@admin.register(UserPreferences)
class PreferencesAdmin(admin.ModelAdmin):
    list_display = ("user","email_frequency")
    search_fields = ("user__username",)

@admin.register(NewsletterLog)
class NewsletterLogAdmin(admin.ModelAdmin):
    list_display = ("user","date","status")
    list_filter = ("status","date")
