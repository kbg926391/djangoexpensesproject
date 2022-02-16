from django.shortcuts import render
from django.views import View

# Create your views here.


class RegistrationView(View):
    def get(self, request):
        return render(request,'C:/Users/Berlinmission/Desktop/django-income-expense-website/expenseswebsite/expenseswebsite/templates/authentication/register.html')