from celery import shared_task
from .models import Transaction, Wallet
import time

@shared_task
def process_transaction(transaction_id):
    transaction = Transaction.objects.get(id=transaction_id)
    sender =transaction.sender
    receiver =transaction.receiver

    sender.balance -= transaction.amount
    receiver.balance += transaction.amount
    transaction.status = "success"
    
    sender.save()
    receiver.save()
    transaction.save()

    return "Transaction Successful"