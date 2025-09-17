from rest_framework import viewsets, permissions
from .models import Issue, Feedback
from .serializers import IssueSerializer, FeedbackSerializer


class IssueViewSet(viewsets.ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:  # Admins see all
            return Issue.objects.all()
        return Issue.objects.filter(citizen=user)  # Citizens see only theirs

    def perform_create(self, serializer):
        serializer.save(citizen=self.request.user)


class FeedbackViewSet(viewsets.ModelViewSet):
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.IsAdminUser]  # Only admins can manage feedback

    def get_queryset(self):
        return Feedback.objects.all()
