from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from reports.views import IssueViewSet, FeedbackViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.http import JsonResponse
from accounts.views import RegisterView, LoginView

router = DefaultRouter()
router.register(r'issues', IssueViewSet, basename='issue')
router.register(r'feedback', FeedbackViewSet, basename='feedback')

def home(request):
    return JsonResponse({"message": " placeholder text"})

urlpatterns = [
    path('', home),  # 👈 now root path will respond
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/login/', LoginView.as_view(), name="api_login"),
    path('api/token/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    ]
urlpatterns += [
    path('api/register/', RegisterView.as_view(), name="register"),
]

