from django.urls import path
from . import views

urlpatterns = [
    path('api/quotes/', views.QuoteListCreate.as_view())
]
