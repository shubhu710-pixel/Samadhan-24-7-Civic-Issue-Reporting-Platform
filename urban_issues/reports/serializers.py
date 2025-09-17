from rest_framework import serializers
from .models import Issue, Feedback
from django.contrib.auth.models import User

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['admin_user',"id", "message", "created_at"]

class IssueSerializer(serializers.ModelSerializer):
    feedbacks = FeedbackSerializer(many=True, read_only=True)  # nested feedbacks
    citizen_username = serializers.CharField(source="citizen.username", read_only=True)

    class Meta:
        model = Issue
        # Exclude 'citizen' from writable fields; show username instead
        fields = [
            'id', 'title', 'description', 'category', 'location',
            'status', 'citizen', 'created_at',
            'citizen_username','feedbacks' # <-- Add this line
        ]
        read_only_fields = ['citizen']


    def create(self, validated_data):
        # Automatically assign the logged-in user as the citizen
        user = self.context["request"].user
        return Issue.objects.create(**validated_data)
