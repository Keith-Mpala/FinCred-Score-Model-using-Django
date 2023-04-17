from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import EmploymentInfor, CreditInfor, CreditScore

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone = forms.IntegerField(required=True)

    class Meta:
        model = User
        fields = ["username","first_name", "last_name",  "email", "phone", "password1", "password2"]
        

class EmploymentInforForm(forms.ModelForm):

    class Meta:
        model = EmploymentInfor
        fields = ["Employer","Title","Sector","Contract_type","Date", "Current_employment"]
        
        widgets = {
            'Contract_type': forms.Select(choices=EmploymentInfor.Contract_type_CHOICES),
            'Sector': forms.Select(choices=EmploymentInfor.Sector_CHOICES),
            'Current_employment': forms.CheckboxInput(),
            'Date': forms.DateInput(attrs={'type': 'Date'}),
        }

        labels = {
            'Employer': 'Name of your most recent Employer ',
            'Title':'Job Title ',
            'Sector': 'Industry ',
            'Contract_type': 'Type of Contract ',
            'Date': 'Employment Start Date ',
            'Current_employment': 'Are you currently employed here ',
        }

    # By default Django forms fields are not required. This code makes all fields required by setting 'required' attribute to True
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = True
    


class CreditInforForm(forms.ModelForm):

    class Meta:
        model = CreditInfor
        fields = ["Credit_cards", "Loan_applications", "First_loan", "Total_credit_limit", "Credit_balances", "Overdue_accounts", "Missed_payments","Deliquency", "Bankruptcy"]

        widgets = { 
            'Credit_cards':forms.Select(choices=CreditInfor.Credit_cards_CHOICES),
            'First_loan':forms.Select(choices=CreditInfor.First_loan_CHOICES),
            'Loan_applications':forms.Select(choices=CreditInfor.Loan_applications_CHOICES),
            'Credit_balances':forms.Select(choices=CreditInfor.Credit_balances_CHOICES),
            'Missed_payments':forms.Select(choices=CreditInfor.Missed_payments_CHOICES),
            'Deliquency':forms.Select(choices=CreditInfor.Deliquency_CHOICES ),
        }

        labels = {
            'Credit_cards': 'How many credit cards do you have? ',
            'Deliquency':'What is the most delinquent you have ever been on a loan or credit card payment? ',
            'Missed_payments':'When did you last miss a loan or credit card payment? ',
            'Credit_balances':'Besides any mortgage loans, what are your total balances on all other loans and credit cards combined? ',
            'Loan_applications':'How many loans or credit cards have you applied for in the last year? ',
            'First_loan': 'How long ago did you get your first loan? (i.e., auto loan, mortgage, student loan, etc.) ',
            'Total_credit_limit':'What percent of your total credit card limits do your credit card balances represent? (0 - 100%) ',
            'Overdue_accounts':'How many of your loans and/or credit cards are currently past due? ',
            'Bankruptcy': 'In the last 10 years, have you ever experienced bankruptcy, repossession or an account in collections? ',
        }



class CreditScoreForm(forms.ModelForm):

    class Meta:
        model = CreditScore
        fields = ['score_infor', 'credit_score']
