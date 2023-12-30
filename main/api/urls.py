from django.urls import path
from .views import CapitalizeTextView

urlpatterns = [
    path('capitalize/', CapitalizeTextView.as_view(), name='capitalize-text'),
]
