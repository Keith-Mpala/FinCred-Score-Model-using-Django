
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, EmploymentInforForm, CreditInforForm
from FinCred.models import EmploymentInfor, CreditInfor, CreditScore
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):

    return render(request, "FinCred/home.html") 

# function for sign up page
def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)  # creates a new form
        if form.is_valid():
            user = form.save(commit=False)  # this creates new user profile before saving
            user.save()
           # profile = UserProfile.objects.create(user=user, employment_info=form.cleaned_data['employment_info'])
            login(request, user)  # after successfuly creating user, we try to login new user
            # redirects the user to the sign in page
            return redirect('/login')
    else:
        form = RegisterForm()
    return render(request, "registration/sign_up.html", {"form": form})


# function for employment model
@login_required(login_url="/login")
def employment_details(request):
    #try:
        # retrieve the object/instance of the EmploymentInfor model where employment_infor matches request.user
        #employment = EmploymentInfor.objects.get(employment_infor=request.user)
    #except EmploymentInfor.DoesNotExist:
        #employment = None

    if request.method == "POST":
        employment_form = EmploymentInforForm(request.POST) #, instance=employment
        if employment_form.is_valid():
            employment_form = EmploymentInfor()
            # include foreign key "employment_infor" to the form before saving it
            #employment = employment_form.save(commit=False)

            employment_form.employment_infor = request.user
            # set the fields from the form data
            employment_form.Employer = employment_form.cleaned_data['Employer']
            employment_form.Title = employment_form.cleaned_data['Title']
            employment_form.Sector = employment_form.cleaned_data['Sector']
            employment_form.Contract_type = employment_form.cleaned_data['Contract_type']
            employment_form.Date = employment_form.cleaned_data['Date']
            employment_form.Current_employment = employment_form.cleaned_data['Current_employment']
            employment_form.save()
            #employment = employment_form.save()
            return render(request, 'FinCred/credit_details.html')
        
    else:
        # pass existing employment object to the form if it exists, otherwise create a new instance
        employment_form = EmploymentInforForm()#instance=employment
    return render(request, 'FinCred/employment_details.html', {'employment_form': employment_form})



@login_required(login_url="/login")
def credit_details(request):
    # here we retrieve instance 'employment_infor' from EmploymentInfor model that is used to query the Credit_Infor model to retrieve a single instance 'credit_infor
    #employment_info = EmploymentInfor.objects.get(employment_infor=request.user)
    # if employment_info exists, retrieve the related credit object, otherwise set credit to None
    #credit = CreditInfor.objects.get(credit_infor=employment_info)
    try:
        # now connected the credit infor to user
        credit = CreditInfor.objects.get(credit_infor=request.user)
    except CreditInfor.DoesNotExist:
        credit = None
    
    if request.method == "POST":
        credit_form = CreditInforForm(request.POST, instance=credit)
        if credit_form.is_valid():
            Credit_cards = credit_form.cleaned_data['Credit_cards']
            Overdue_accounts = credit_form.cleaned_data['Overdue_accounts']
            Deliquency = credit_form.cleaned_data['Deliquency']
            Missed_payments = credit_form.cleaned_data['Missed_payments']
            Credit_balances = credit_form.cleaned_data['Credit_balances']
            Loan_applications = credit_form.cleaned_data['Loan_applications']
            First_loan = credit_form.cleaned_data['First_loan']
            Total_credit_limit = credit_form.cleaned_data['Total_credit_limit']
            Bankruptcy = credit_form.cleaned_data['Bankruptcy']
            
            variables = [[Credit_cards, Overdue_accounts, Deliquency, Missed_payments, Credit_balances, 
                        Loan_applications, First_loan, Total_credit_limit, Bankruptcy]]
            
            # Used for calculating the credit score for all 8 variables
            score = 850
            weight_1 = 0.1 * score 
            weight_2 = 0.2 * score 

            variable_1 = int(Credit_cards)
            if variable_1 == 2:
                value_1 = int(weight_1)
            elif variable_1 == 3:
                value_1 = int(weight_1*0.95)
            elif variable_1 == 1:
                value_1 = int(weight_1*0.85)
            elif variable_1 == 0:
                value_1 = int(weight_1*0.7)
            else:
                value_1 = int(weight_1*0.8)


            variable_2 = int(Loan_applications)
            if variable_2 == 0:
                value_2 = int(weight_1*0.85)
            elif variable_2 == 1:
                value_2 = int(weight_1*0.95)
            elif variable_2 == 2:
                value_2 = int(weight_1)
            elif variable_2 == 3:
                value_2 = int(weight_1*0.90)
            else:
                value_2 = int(weight_1*0.80)


            variable_3 = int(First_loan)
            if variable_3  == 0:
                value_3 = int(weight_1*0.6)
            elif variable_3  == 1:
                value_3 = int(weight_1*0.75)
            elif variable_3  == 2:
                value_3 = int(weight_1*0.80)
            elif variable_3  == 3:
                value_3 = int(weight_1*0.85)
            elif variable_3  == 4:
                value_3 = int(weight_1*0.90)
            elif variable_3  == 5:
                value_3 = int(weight_1*0.95)
            else:
                value_3 = int(weight_1)


            variable_4 = int(Total_credit_limit)
            if 0 < variable_4 < 20:
                value_4 = int(3*weight_1*variable_4/100)
            elif 20 <= variable_4 < 40:
                value_4 = int(weight_1*variable_4/100)
            elif 40 <= variable_4 < 60:
                value_4 = int(weight_1*variable_4/100)
            elif 60 <= variable_4 < 70:
                value_4 = int(weight_1*variable_4/100)
            elif 70 <= variable_4 <= 100:
                value_4 = int(weight_1*variable_4/100)
            else:
                value_4 = 0


            variable_5 = int(Credit_balances)
            if variable_5 == 0:
                value_5 = int(weight_1*0.85)
            elif variable_5 == 1:
                value_5 = int(weight_1*0.90)
            elif variable_5 == 2:
                value_5 = int(weight_1)
            elif variable_5 == 3:
                value_5 = int(weight_1*0.95)
            elif variable_5 == 4:
                value_5 = int(weight_1*0.8)
            else:
                value_5 = int(weight_1*0.7)


            variable_6 = int(Overdue_accounts)
            if variable_6 == 0:
                value_6 = int(weight_2)
            elif variable_6 == 1:
                value_6 = int(weight_2*0.95)
            elif variable_6 == 2:
                value_6 = int(weight_2*0.85)
            elif variable_6 == 3:
                value_6 = int(weight_2*0.8)
            elif variable_6 == 4:
                value_6 = int(weight_2*0.7)
            elif variable_6 == 5:
                value_6 = int(*weight_2*0.6)
            else:
                value_6 = int(weight_2*0.5)


            variable_7 = int(Missed_payments)
            if variable_7 == 0:
                value_7 = int(weight_1)
            elif variable_7 == 1:
                value_7 = int(weight_1*0.60)
            elif variable_7 == 2:
                value_7 = int(weight_1*0.65)
            elif variable_7 == 3:
                value_7 = int(weight_1*0.75)
            elif variable_7 == 4:
                value_7 = int(weight_1*0.80)
            elif variable_7 == 5:
                value_7 = int(weight_1*0.85)
            else:
                value_7 = int(weight_1*0.90)


            variable_8 = int(Deliquency)
            if variable_8 == 0:
                value_8 = int(weight_1)
            elif variable_8 == 1:
                value_8 = int(weight_1*0.95)
            elif variable_8 == 2:
                value_8 = int(weight_1*0.85)
            elif variable_8 == 3:
                value_8 = int(weight_1*0.75)
            else:
                value_8 = int(weight_1*0.5)
            
            # sum up the variables  
            result = value_1 + value_2 + value_3 + value_4 + value_5 + value_6 + value_7 + value_8 

            # variable to check if bankrupty or not
            if Bankruptcy:
                final_score = result - 50
            else:
                final_score = result + 75

            # save the form to the Credit_infor model
            credit = credit_form.save(commit=False)
            #employment_info = EmploymentInfor.objects.get(employment_infor=request.user)
            credit.credit_infor = request.user #employment_info
            credit.save()

            # create a new instance of CreditScore model and set its attributes so that we add the result of credit_score to the model
            score_instance = CreditScore()
            score_instance.score_infor = request.user
            score_instance.credit_score = final_score
            score_instance.timestamp = timezone.now()

            # save the instance to the database
            score_instance.save()

            context = {'final_score': final_score}

            return render(request, 'FinCred/credit_score.html',  context )
    else:

        credit_form = CreditInforForm(instance=credit)
    return render(request, 'FinCred/credit_details.html', {'credit_form': credit_form})


def credit_score(request):
    
    return render(request, 'FinCred/credit_score.html')







