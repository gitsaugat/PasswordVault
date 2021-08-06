from django.contrib.auth import login
from django.shortcuts import render
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from .models import Password
# Create your views here.

HOMEPAGE_DECORATORS = [ login_required ]

@method_decorator(HOMEPAGE_DECORATORS , name="get")
class HomePage(View):
    
    def get(self , request , **kwargs):
        context = kwargs
        context['title'] = 'Dashboard'
        context['passwords'] = self.get_user_passwords(request.user)
        return render(request , 'manager/index.html' , context )
    
    def get_user_passwords(self , user):
        try:
            passwords = Password.objects.filter( user = user )
        except Password.DoesNotExist:
            return []
        return passwords

    
