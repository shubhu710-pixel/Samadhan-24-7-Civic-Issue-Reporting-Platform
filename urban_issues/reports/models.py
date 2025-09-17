from django.db import models
from django.contrib.auth.models import User

class Issue(models.Model):
    CATEGORY_CHOICES = [
        ("pothole", "Pothole"),
        ("streetlight", "Broken Streetlight"),
        ("sanitation", "Sanitation"),
        ("other", "Other"),
    ]

    STATUS_CHOICES = [
        ("reported", "Reported"),
        ("in_progress", "In Progress"),
        ("resolved", "Resolved"),
    ]

    citizen = models.ForeignKey(User, on_delete=models.CASCADE, related_name="issues")
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    location = models.CharField(max_length=255)  # could integrate with Google Maps API
    image = models.ImageField(upload_to="issue_images/", blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="reported")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.status}"


class Feedback(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name="feedbacks")
    admin_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="feedback_given")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Feedback for Issue #{self.issue.id}"
