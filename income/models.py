from django.db import models
from django.conf import settings

# Create your models here.


class Income(models.Model):

    SOURCE_CATEGORY = [
        ('Salary', 'Salary'),
        ('Gift', 'Gift'),
        ('Freelance', 'Freelance'),
        ('Loan', 'Loan'),
        ('Business', 'Business'),
    ]

    source = models.CharField(choices=SOURCE_CATEGORY, max_length=255)
    owner = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField()
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, max_length=255)
    date = models.DateField(null=False, blank=False)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return str(self.owner) + ' income'
