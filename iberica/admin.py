from django.contrib import admin
from .models import Tourism
# Register your models here.
#admin:username-iberica2022
#admin:password-ibericalcn
admin.site.login_form='Iberica'
admin.site.register(Tourism)