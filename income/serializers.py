from rest_framework import serializers
from django.conf import settings


from .models import Income


class IncomeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Income
        fields = ['id', 'source', 'description', 'amount', 'date']
