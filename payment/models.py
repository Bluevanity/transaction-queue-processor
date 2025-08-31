from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=00.00)
    
    def __str__(self):
        return f"{self.user.username}'s Wallet"


class Transaction(models.Model):
    sender = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name="sent")
    receiver = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name="received")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(default="pending")