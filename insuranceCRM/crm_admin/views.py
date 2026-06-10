from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from crm_admin.models import AgentModel,CampaginModel
from agent.models import ClientModel
import random
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.

def admin_dashboard(request):
    ta = AgentModel.objects.all().count()
    tc = CampaginModel.objects.all().count()
    tcl = ClientModel.objects.all().count()
    return render(request,'dashboard.html',{'ta':ta,'tc':tc,'tcl':tcl})


def add_agent(request):
    return render(request,'add_agent.html')

def addagent(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        pnumber = request.POST['pnumber']
        specialization = request.POST['specialization']
        email = request.POST['email']
        uname = request.POST['uname']
        image=request.FILES.get('file')


        if image==None:
            image="images/default.png"        
        
        # Generate random 6 digit password
        password = str(random.randint(100000,999999))

        user = User.objects.create_user(first_name=fname,
                                        last_name = lname,
                                        email = email,
                                        username=uname,
                                        password=password,
                                        )
        user.save()

        user_data = User.objects.get(id=user.id)
        agent_data = AgentModel( 
                                pnumber=pnumber,
                                admin = user_data,
                                specialization = specialization,
                                image=image,
                                )
        agent_data.save()

        subject = "Welcome to Our Agency"

        message = f"""
        Hello {fname},

        Welcome to Incurunse CRM 
        Your account has been created successfully. Below are your login details:

        Username : {uname}
        Password : {password}

        Please keep your credentials safe and do not share them with anyone.

        Thank you for joining us!

        Best Regards,  
        Incurunse CRM Team
        """

        recipient = email
        send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
        messages.success(request,'Add Agent Successfully')
        return redirect("view_agent")

def check_agent_data(request):
    email = request.GET.get("email")
    username = request.GET.get("username")
    phone = request.GET.get("phone")

    data = {
        "email_exists": False,
        "username_exists": False,
        "phone_exists": False
    }

    if email:
        data["email_exists"] = User.objects.filter(email=email).exists()

    if username:
        data["username_exists"] = User.objects.filter(username=username).exists()

    if phone:
        data["phone_exists"] = AgentModel.objects.filter(pnumber=phone).exists()

    return JsonResponse(data)

def edit_agent_data(request):
    user_id = request.GET.get('id')

    email = request.GET.get('email')
    username = request.GET.get('username')
    phone = request.GET.get('phone')

    data = {
        'email_exists': False,
        'username_exists': False,
        'phone_exists': False
    }

    if email:
        data['email_exists'] = User.objects.filter(
            email=email
        ).exclude(id=user_id).exists()

    if username:
        data['username_exists'] = User.objects.filter(
            username=username
        ).exclude(id=user_id).exists()

    if phone:
        data['phone_exists'] = AgentModel.objects.filter(
            pnumber=phone
        ).exclude(admin_id=user_id).exists()

    return JsonResponse(data)

def view_agent(request):
    agent = AgentModel.objects.all()
    return render(request,'view_agent.html',{'datas':agent})

def edit_agent(request,pk):
    agent = AgentModel.objects.get(id=pk)
    return render(request,"edit_agent.html",{'data':agent})

def editagent(request,pk):
    agent = AgentModel.objects.get(id=pk)
    if request.method == 'POST':
        # Update User table (IMPORTANT: save it separately)
        user = agent.admin
        user.first_name = request.POST['fname']
        user.last_name = request.POST['lname']
        user.email = request.POST['email']
        user.save()

        # Update Agent table
        
        agent.pnumber = request.POST['pnumber']
         
        agent.specialization = request.POST['specialization']
        old = agent.image
        new = request.FILES.get("file")
        if new:
            agent.image = new
        else:
            agent.image = old

        agent.save()
        messages.success(request,'Edit Agent Successfully')
        return redirect('view_agent')
    else:
        return redirect('edit_agent')
    
def delete_agent(request,pk):
    data = AgentModel.objects.get(id=pk)
    admin = data.admin
    admin.delete()
    data.delete()
    messages.success(request,'Delete Agent Successfully')
    return redirect('view_agent')

def add_campagin(request):
    agent = AgentModel.objects.all()
    return render(request,'add_campagin.html',{'agent':agent})

def addcampagin(request):
    if request.method == 'POST':
        name = request.POST['name']
        agent_id = request.POST['agent']
        date = request.POST['date']
        time = request.POST['time']
        location =  request.POST['location']

        agent_date  = AgentModel.objects.get(id=agent_id)
        campagin = CampaginModel(name=name,
                                 date = date,
                                 time = time,
                                 location = location,
                                 agent = agent_date,
                                )
        campagin.save()
        messages.success(request,'Add Campagin Successfully')
        return redirect('view_campagin')



def view_campagin(request):
    campagin = CampaginModel.objects.all()
    return render(request,'view_campagin.html',{'datas':campagin})

def edit_campagin(request,pk):
    campagin = CampaginModel.objects.get(id=pk)
    agent = AgentModel.objects.all()
    return render(request,'edit_campagin.html',{'data':campagin,'agent':agent})

def editcampagin(request,pk):
    campagin = CampaginModel.objects.get(id=pk)
    if request.method == 'POST':
        campagin.name = request.POST['name']
        campagin.agent_id = request.POST['agent']
        campagin.date = request.POST['date']
        campagin.time = request.POST['time']
        campagin.location = request.POST['location']
        campagin.save()
        messages.success(request,'Edit Campagin Successfully')
        return redirect('view_campagin')
    
def delete_campagin(request,pk):
    data = CampaginModel.objects.get(id=pk)
    data.delete()
    messages.success(request,'Delete Campagin Successfully')
    return redirect('view_campagin')

def view_total_client(request):
    clients = ClientModel.objects.all()
    return render(request,'view_total_client.html',{'clients':clients})
 