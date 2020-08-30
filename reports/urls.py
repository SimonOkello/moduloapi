from django.urls import path


from .views import ExpenseStatistics, IncomeStatistics


urlpatterns = [
    path('expense_category/',ExpenseStatistics.as_view(), name= 'expense-category'),
    path('income_source/',IncomeStatistics.as_view(), name= 'income-category'),
    
]