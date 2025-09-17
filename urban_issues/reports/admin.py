# reports/admin.py

from django.contrib import admin
from .models import Issue, Feedback

class FeedbackInline(admin.TabularInline):
    model = Feedback
    extra = 1  # Number of empty forms to display
    # Add 'text' and 'user' to the fields to display
    fields = ['text', 'user']

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'created_at', 'citizen']
    list_filter = ['status', 'created_at']
    search_fields = ['title', 'description', 'location']
    
    inlines = [FeedbackInline]
    
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    # Change these names to match the fields in your Feedback model
    list_display = ['issue', 'message', 'created_at', 'admin_user'] 
    list_filter = ['created_at']
    search_fields = ['text']
