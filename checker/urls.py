from django.urls import path
from .views import CHECK


urlpatterns = [
    path('check/', CHECK.as_view(), name="check_plagiarism")
]