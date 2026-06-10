from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from crm_admin.models import AgentModel
from django.contrib import messages
 

# Create your views here.

def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')



def submit_login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pword = request.POST['password']

    if not User.objects.filter(username=uname).exists():
            messages.error(request, "Username does not exist")
            return redirect('login')
    
    user = auth.authenticate(username=uname,password=pword)

    if user is None:
            messages.error(request, "Incorrect password")
            return redirect('login')
    

    
    auth.login(request,user)

    if user.is_superuser:
        messages.success(request, f'Welcome {uname}')
        return redirect('admin_dashboard')
    
    elif AgentModel.objects.filter(admin=user).exists():
        messages.success(request, f'Welcome {uname}')
        return redirect('agent_dashboard')
         

def logout(request):
    auth.logout(request)
    messages.error(request,'Logout Successfully')
    return redirect('login')

