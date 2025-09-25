from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Article, Bookmark, UserPreferences, NewsletterLog

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","username","email","first_name","last_name")

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ("username","email","password","first_name","last_name")

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email",""),
            password=validated_data["password"],
            first_name=validated_data.get("first_name",""),
            last_name=validated_data.get("last_name","")
        )
        return user

class UserPreferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPreferences
        fields = ("categories","email_frequency")

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("id","title","summary","full_content","category","date","source_url")

class BookmarkSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(read_only=True)
    article_id = serializers.PrimaryKeyRelatedField(queryset=Article.objects.all(), write_only=True, source="article")
    class Meta:
        model = Bookmark
        fields = ("id","article","article_id","created_at")

class NewsletterLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterLog
        fields = ("id","user","date","status","details")
        read_only_fields = ("user","date")
