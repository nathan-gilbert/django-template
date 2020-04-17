from .models import Quotes
from .serializers import QuoteSerializer
from rest_framework import generics


class QuoteListCreate(generics.ListCreateAPIView):
    queryset = Quotes.objects.all()
    serializer_class = QuoteSerializer
