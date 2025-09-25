# core/management/commands/generate_daily_digest.py
from django.core.management.base import BaseCommand
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import timezone

from core.models import User, Article, NewsletterLog
from core.llm_client import fetch_daily_insights

class Command(BaseCommand):
    help = "Generate daily digest using Gemini API and send newsletters."

    def handle(self, *args, **kwargs):
        self.stdout.write("🚀 Starting daily digest generation...")

        categories = ["AI", "Cybersecurity", "Finance", "Health", "Science", "Technology"]
        insights = fetch_daily_insights(categories)

        # Store insights in DB as Article objects
        for category, summary in insights.items():
            Article.objects.create(
                title=f"Daily {category} Digest - {timezone.now().strftime('%Y-%m-%d')}",
                summary=summary,
                category=category,
                full_content=summary,
                date=timezone.now().date(),
                source="Gemini API"
            )

        # Send emails to users
        for user in User.objects.all():
            preferred = user.preferences.get("categories", categories)

            user_articles = Article.objects.filter(
                category__in=preferred,
                date=timezone.now().date()
            )

            html_content = render_to_string(
                "core/email_templates/newsletter.html",
                {"user": user, "articles": user_articles}
            )

            email = EmailMultiAlternatives(
                subject="📩 Your Daily AI Research Digest",
                body="Here are your daily insights.",
                from_email="noreply@aidigest.com",
                to=[user.email],
            )
            email.attach_alternative(html_content, "text/html")

            try:
                email.send()
                NewsletterLog.objects.create(user=user, date=timezone.now().date(), status="SENT")
                self.stdout.write(self.style.SUCCESS(f"✅ Newsletter sent to {user.email}"))
            except Exception as e:
                NewsletterLog.objects.create(user=user, date=timezone.now().date(), status=f"FAILED: {str(e)}")
                self.stdout.write(self.style.ERROR(f"❌ Failed to send to {user.email}: {e}"))

        self.stdout.write("🎉 Daily digest process completed.")
