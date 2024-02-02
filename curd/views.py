# views.py
from rest_framework import generics
from .models import Webhook
from .serializers import WebhookSerializer

class WebhookListCreateView(generics.ListCreateAPIView):
    queryset = Webhook.objects.all()
    serializer_class = WebhookSerializer

class WebhookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Webhook.objects.all()
    serializer_class = WebhookSerializer
