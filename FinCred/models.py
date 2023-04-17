from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from datetime import date


# from .models import UserProfile

# Create your models here.
# we use lazy referencing instead of direct passing of direct referencing the classes; 

#class UserProfile(models.Model):
   # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
   # employment_info = models.OneToOneField('EmploymentInfor', on_delete=models.CASCADE)
    #credit_info = models.ForeignKey('CreditInfor', on_delete=models.CASCADE, related_name='user_profiles')


class EmploymentInfor(models.Model):

    Contract_type_CHOICES = [
        ('Full-time', 'Full-time'),
        ('Part-time','Part-time'),
        ('Contract','Fixed-term Contract'),
        ('Freelance Contract','Freelance Contract'),
        ('Self-employed','Self-employed'),

    ]

    Sector_CHOICES = [  
        ('Self-employed', 'Self-employed'),
        ('Retail Trade', 'Retail Trade'),
        ('Construction','Construction'),  
        ('Agriculture','Agriculture'),
        ('Manufacturing','Manufacturing'), 
        ('Wholesale Trade','Wholesale Trade'),
        ('Finance and Insurance','Finance and Insurance'), 
        ('Education and Training','Education and Training'), 
        ('Transportation and Warehousing','Transportation and Warehousing'),
        ('Accommodation and Food Services','Accommodation and Food Services'), 
        ('Healthcare and Social Assistance','Healthcare and Social Assistance'),
        ('Professional, Scientific, and Technical Services','Professional, Scientific, and Technical Services'),     
    ]
    # one-to-one relationship with the user which connects it tocurrently logged-in user
    # define form fields
    
    Employer = models.CharField(max_length=50)
    Title = models.CharField(max_length=50)
    Sector = models.CharField(max_length=50, choices=Sector_CHOICES)
    Contract_type = models.CharField(max_length=80, choices=Contract_type_CHOICES)
    Date = models.DateField(default=date.today)
    Current_employment = models.BooleanField(default=False)
    employment_infor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


class CreditInfor(models.Model):

    Credit_cards_CHOICES = [
        ('0', 'I have never had a credit card'),
        ('1', 'Only 1'),
        ('2', '2 to 3'),
        ('3', '4 to 6'),
        ('4', '5 or more'),   
    ]
    First_loan_CHOICES = [
        ('0', 'I have never had a loan'),
        ('1','less than 6 months ago'),
        ('2','between 6 months and 2 years ago'),
        ('3','2 to 5 years ago'),
        ('4','5 to 10 years ago'),
        ('5','10 to 15 years ago'),
        ('6', 'more than 15 years ago'),
    ]

    Loan_applications_CHOICES = [
        ('0','None'),
        ('1','1'),
        ('2','2'),
        ('3','3 to 5'),
        ('4', '6 or more'),
    ]

    Credit_balances_CHOICES = [
        ('0','I only have mortgage loan(s)'),
        ('1','Less than $500'),
        ('2','$500 to $999'),
        ('3','$1000 to $4,999'),
        ('4', '$5000 to $9,999'),
        ('5', '$10,000+'),
        
    ]

    Missed_payments_CHOICES = [
        ('0', 'I have never missed a payment'),
        ('1','In the past 3 months'),
        ('2','3 to 6 months ago'),
        ('3','6 months to 1 year ago'),
        ('4','1 to 2 years ago'),
        ('5','2 to 4 years ago'),
        ('6', 'more than 4 years ago'),
    ]

    Deliquency_CHOICES = [
        ('0','None'),
        ('1','30 days deliquent'),
        ('2','60 days deliquent'),
        ('3','90 days deliquent'),
        ('4', 'More than 90 days deliquent'),
    ]

    Credit_cards = models.CharField(max_length=50, choices=Credit_cards_CHOICES)
    Overdue_accounts = models.PositiveIntegerField()
    Deliquency = models.CharField(max_length=50, choices=Deliquency_CHOICES)
    Missed_payments= models.CharField(max_length=50, choices=Missed_payments_CHOICES)
    Credit_balances = models.CharField(max_length=50, choices=Credit_balances_CHOICES)
    Loan_applications = models.CharField(max_length=50, choices=Loan_applications_CHOICES)
    First_loan = models.CharField(max_length=50, choices=First_loan_CHOICES)
    Total_credit_limit = models.PositiveIntegerField()
    Bankruptcy = models.BooleanField(default=False)
    #credit_infor = models.ForeignKey(EmploymentInfor, on_delete=models.CASCADE)
    credit_infor = models.ForeignKey(User, on_delete=models.CASCADE)
    

class CreditScore(models.Model):
    score_infor = models.ForeignKey(User, on_delete=models.CASCADE)
    credit_score = models.DecimalField(max_digits=5, decimal_places=2)
    

    #def __str__(self):
        #return str(self.id)
