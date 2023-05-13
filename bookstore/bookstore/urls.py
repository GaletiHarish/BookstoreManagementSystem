from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from.views import BookViewSet, CustomerViewSet, TransactionViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='books')
router.register(r'customers', CustomerViewSet, basename='customers')
router.register(r'transactions', TransactionViewSet, basename='transactions')

urlpatterns = [
    path('', include(router.urls)),
]
