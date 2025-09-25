from django.db import models

# Create your models here.
from django.contrib.auth.models import User

CATEGORIES = [
    ("AI", "Artificial Intelligence"),
    ("CYBER", "Cybersecurity"),
    ("FINANCE", "Finance & FinTech"),
    ("HEALTH", "Healthcare & Biotech"),
    ("CLIMATE", "Climate & Sustainability"),
    ("SPACE", "Space & Emerging Tech"),
    ("EDU", "Education & EdTech"),
]

FREQUENCY_CHOICES = [
    ("daily", "Daily"),
    ("weekly", "Weekly"),
]

class UserPreferences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="preferences")
    categories = models.JSONField(default=list, blank=True)  # e.g. ["AI","CYBER"]
    email_frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES, default="daily")

    def __str__(self):
        return f"Prefs({self.user.username})"

class Article(models.Model):
    title = models.CharField(max_length=512)
    summary = models.TextField()
    full_content = models.TextField(blank=True)
    category = models.CharField(max_length=32, choices=CATEGORIES)
    date = models.DateField(auto_now_add=True)
    source_url = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.title} [{self.category}]"

class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookmarks")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="bookmarked_by")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "article")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.username} -> {self.article.id}"

class NewsletterLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="newsletter_logs")
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[("sent","Sent"),("failed","Failed")])
    details = models.TextField(blank=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"NewsletterLog({self.user.username}, {self.status})"