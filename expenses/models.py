from django.db import models
from django.conf import settings

# Create your models here.


class Expense(models.Model):

    EXPENSE_CATEGORY = [
        ('Travel', 'Travel'),
        ('Rent', 'Rent'),
        ('Food', 'Food'),
        ('Internet', 'Internet'),
        ('Electricity', 'Electricity'),
        ('Vacation', 'Vacation'),
        ('Netflix', 'Netflix'),
        ('Other', 'Other'),
    ]

    category = models.CharField(choices=EXPENSE_CATEGORY, max_length=255)
    owner = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField()
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, max_length=255)
    date = models.DateField(null=False, blank=False)
