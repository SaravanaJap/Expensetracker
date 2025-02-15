from django.db import models
from accounts.models import Account

# Create your models here.

class Expense(models.Model):
    EXPENSE = 'expense'
    INCOME = 'income'
    TRANSACTION_TYPE_CHOICES = [
        (EXPENSE, 'Expense'),
        (INCOME, 'Income'),
    ]
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    cost = models.IntegerField()
    category = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    user = models.ForeignKey(Account,on_delete=models.CASCADE,null=True)
    transaction_type = models.CharField(max_length=7, choices=TRANSACTION_TYPE_CHOICES, default=EXPENSE)