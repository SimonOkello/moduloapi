from rest_framework import serializers
from django.conf import settings


from .models import Expense

class ExpenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expense
        fields = ['category', 'description', 'amount', 'date' ]