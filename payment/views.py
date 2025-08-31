from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status
from django.http import JsonResponse
from rest_framework.response import Response
from .models import Transaction, Wallet
from .serializers import RegisterSerializer, TransactionSerializer, WalletSerializer
from .tasks import process_transaction
# Create your views here.

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

class TransactionCreateView(generics.CreateAPIView):
    queryset = Transaction.objects.all()
    permisssion_classes = [permissions.IsAuthenticated]
    serializer_class = TransactionSerializer

    def create(self, request):
        wallet = Wallet.objects.get(user=self.request.user)
        transaction = Transaction.objects.create(
            sender=wallet,
            receiver=Wallet.objects.get(id=request.data.get("receiver")),
            amount=request.data.get("amount"),
        )
        result = process_transaction.delay(transaction.id)
        return Response(TransactionSerializer(transaction).data, status=status.HTTP_201_CREATED)

class WalletDetailView(generics.RetrieveAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    