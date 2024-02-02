# urls.py
from django.urls import path
from .views import WebhookListCreateView, WebhookDetailView

urlpatterns = [
    path('webhooks/', WebhookListCreateView.as_view(), name='webhook-list-create'),
    path('webhooks/<int:pk>/', WebhookDetailView.as_view(), name='webhook-detail'),
]
# urls.py
from django.urls import path
from .views import WebhookListCreateView, WebhookDetailView

urlpatterns = [
    path('webhooks/', WebhookListCreateView.as_view(), name='webhook-list-create'),
    path('webhooks/<int:pk>/', WebhookDetailView.as_view(), name='webhook-detail'),
]

from django.contrib import admin
from django.urls import include, path


