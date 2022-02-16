from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'C:/Users/Berlinmission/Desktop/django-income-expense-website/expenseswebsite/expenseswebsite/templates/expenses/index.html')


def add_expense(request):
    return render(request,'C:/Users/Berlinmission/Desktop/django-income-expense-website/expenseswebsite/expenseswebsite/templates/expenses/add_expense.html')
