from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, status, generics
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from .models import Article, Bookmark, UserPreferences, NewsletterLog
from .serializers import (
    ArticleSerializer, BookmarkSerializer, UserSerializer,
    RegisterSerializer, UserPreferencesSerializer, NewsletterLogSerializer
)

# --- Registration endpoint
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

# --- User view for profile (optional)
class CurrentUserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

# --- Articles (public read)
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by("-date")
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    http_method_names = ["get","post","put","patch","delete"]
    filterset_fields = ["category","date"]
    search_fields = ["title","summary","full_content"]

    def get_permissions(self):
        if self.action in ["create","update","partial_update","destroy"]:
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]

# --- Bookmarks
class BookmarkViewSet(viewsets.ModelViewSet):
    serializer_class = BookmarkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Bookmark.objects.filter(user=self.request.user).select_related("article")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# --- Preferences
class PreferencesView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserPreferencesSerializer

    def get_object(self):
        prefs, _ = UserPreferences.objects.get_or_create(user=self.request.user)
        return prefs

# --- Newsletter Logs (user)
class NewsletterLogViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = NewsletterLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return NewsletterLog.objects.filter(user=self.request.user)
