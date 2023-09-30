from django.urls import path
from .views import InvoiceViewSet

urlpatterns = [
    path('', InvoiceViewSet.as_view({'get': 'list', 'post': 'create'}), name='InvoiceView'),
    path('<int:pk>/', InvoiceViewSet.as_view({'get': 'retrieve'}), name='invoice-detail'),  # Add this line
]
