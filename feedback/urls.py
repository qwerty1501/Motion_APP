from django.urls import path
from .views import FeedbackLinkCreateListView, FeedbackLinkDeleteView


urlpatterns = [
    path('feedback/link/', FeedbackLinkCreateListView.as_view()),
    path('feedback/link/delete/<int:pk>/', FeedbackLinkDeleteView.as_view()),
]