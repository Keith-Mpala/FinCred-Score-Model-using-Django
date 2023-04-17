from django.contrib import admin
from django.contrib.auth.models import User
from .models import EmploymentInfor, CreditInfor, CreditScore

# Register your models here.
# creating the custom admin class to enable customising the behavior of the admin interface for the models

class EmploymentInfoAdmin(admin.ModelAdmin):
    pass

class CreditInfoAdmin(admin.ModelAdmin):
    pass

class CreditScoreAdmin(admin.ModelAdmin):
    pass


admin.site.register(EmploymentInfor, EmploymentInfoAdmin)
admin.site.register(CreditInfor, CreditInfoAdmin)
admin.site.register(CreditScore, CreditScoreAdmin)
