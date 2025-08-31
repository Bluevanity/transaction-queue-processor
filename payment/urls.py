from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RegisterView, TransactionCreateView, WalletDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('transfer/', TransactionCreateView.as_view(), name='transfer'),
    path('wallet/<pk>/', WalletDetailView().as_view(), name='get_wallet')
]
