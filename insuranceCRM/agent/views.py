from django.shortcuts import render,redirect
from crm_admin.models import AgentModel,CampaginModel
from agent.models import ClientModel
from datetime import date
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.models import auth,User

# Create your views here.
today = date.today()
def agent_dashboard(request):
    user = request.user
    agent = AgentModel.objects.get(admin=user)
    total_campagin = CampaginModel.objects.filter(agent_id=agent).count()
    total_client = ClientModel.objects.filter(agent_id = agent).count()
    today_campagin = CampaginModel.objects.filter(agent_id=agent,date=today).count()
    return render(request,"agent_dashboard.html",{'data':agent,'tc':total_campagin,'tcl':total_client,'toc':today_campagin})

def update_agent(request):
    user = request.user
    agent = AgentModel.objects.get(admin=user)
    return render(request,"update_profile.html",{'data':agent})

def updateagent(request):
    user = request.user
    agent = AgentModel.objects.get(admin=user)
    
    if request.method == 'POST':
         
        user = agent.admin
        user.first_name = request.POST['fname']
        user.last_name = request.POST['lname']
        user.email = request.POST['email']
        user.username = request.POST['uname']
         
        
        user.save()

        agent.pnumber = request.POST['pnumber']
        agent.specialization = request.POST['specialization']
        old = agent.image
        new = request.FILES.get("file")
        if new:
            agent.image = new
        else:
            agent.image = old

        agent.save()
        messages.success(request,'Update profile Successfully')
        return redirect('agent_dashboard')

def change_password(request):
    user = request.user
    agent = AgentModel.objects.get(admin=user)
    
    return render(request,"change_password.html",{'data':agent})

def changepassword(request):

    user = request.user

    if request.method == "POST":

        new_password = request.POST.get("npassword")
        confirm_password = request.POST.get("cpassword")
        
        # Password match
        if new_password == confirm_password:

            user.set_password(new_password)
            user.save()
            messages.success(request,'Change Password Successfully')
            return redirect("logout")

def check_agent_profile(request):
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


def view_agent_campagin(request):
    user = request.user
    agent = AgentModel.objects.get(admin=user)
    campaigns = CampaginModel.objects.filter(agent_id=agent)

    return render(request,'view_agent_campagin.html',{'datas':campaigns,'data':agent})

def add_client(request):
    user = request.user
    agent = AgentModel.objects.get(admin=user)
    campaigns = CampaginModel.objects.filter(agent_id=agent)
    return render(request,'add_client.html',{'data':agent,'campagin':campaigns})
def addclient(request):
    user = request.user
    agent = AgentModel.objects.get(admin=user)
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        dob = request.POST['dob']
        pnumber =request.POST['pnumber']
        email = request.POST['email']
        mstatus = request.POST['mstatus']
        aadhaar = request.POST['aadhaar']
        pan_number = request.POST['pan']
        job = request.POST['job']
        qualification = request.POST['qualification']
        campagin = request.POST['campagin']
       
        ppolicy = request.POST['ppolicy']
        ppnumber = request.POST.get('ppnumber')
        ppsame = request.POST.get('ppsame')
        agentf = request.POST['agentf']
        campaginf = request.POST['campaginf']
        image=request.FILES.get('file')
        if image==None:
            image="images/default.png"
        
        agent_data = AgentModel.objects.get(id=agent.id)
        campagin_data = CampaginModel.objects.get(id=campagin)

        client = ClientModel(first_name = fname,
                             last_name = lname,
                             dob=dob,
                             mobile_number=pnumber,
                             married_status = mstatus,
                            aadhaar_number=aadhaar,
                            pan_number=pan_number,
                            email=email,
                            previous_policy=ppolicy,
                            previous_policy_number=ppnumber,
                            same_policy=ppsame,
                            agent_feedback=agentf,
                            campaign_feedback=campaginf,
                            agent = agent_data,
                            campagin=campagin_data,
                            image=image,
                            job=job,
                            qulification=qualification,)
        client.save()
        messages.success(request,'Add Client Successfully')
        return redirect('view_client')

def check_client_data(request):

    email = request.GET.get('email')
    phone = request.GET.get('phone')
    aadhaar = request.GET.get('aadhaar')
    pan = request.GET.get('pan')

    data = {}

    if email:
        data['email_exists'] = ClientModel.objects.filter(email=email).exists()

    if phone:
        data['phone_exists'] = ClientModel.objects.filter(mobile_number=phone).exists()
    
    if aadhaar:
        data['aadhaar_exists'] = ClientModel.objects.filter(aadhaar_number=aadhaar).exists()

    if pan:
        data['pan_exists'] = ClientModel.objects.filter(pan_number=pan).exists()

    return JsonResponse(data)

def check_edit_client_data(request):

    client_id = request.GET.get('client_id')

    email = request.GET.get('email')
    phone = request.GET.get('phone')
    aadhaar = request.GET.get('aadhaar')
    pan = request.GET.get('pan')

    data = {}

    if email:
        data['email_exists'] = ClientModel.objects.filter(email=email).exclude(id=client_id).exists()

    if phone:
        data['phone_exists'] = ClientModel.objects.filter(
            mobile_number=phone
        ).exclude(id=client_id).exists()

    if aadhaar:
        data['aadhaar_exists'] = ClientModel.objects.filter(
            aadhaar_number=aadhaar
        ).exclude(id=client_id).exists()

    if pan:
        data['pan_exists'] = ClientModel.objects.filter(
            pan_number=pan
        ).exclude(id=client_id).exists()

    return JsonResponse(data)

def view_client(request):
    user = request.user
    agent = AgentModel.objects.get(admin=user)
    
    clients = ClientModel.objects.filter(agent=agent.id)
    return render(request,'view_agent_client.html',{'data':agent,'client':clients})

def edit_client(request,pk):
    user = request.user
    agent = AgentModel.objects.get(admin=user)
    clients = ClientModel.objects.get(id=pk)
    campaign = CampaginModel.objects.filter(agent_id=agent)
    return render(request,'edit_client.html',{'data':agent,'client':clients,'campagin':campaign})

def editclient(request,pk):
    client = ClientModel.objects.get(id=pk)
    if request.method == 'POST':
        client.first_name = request.POST['fname']
        client.last_name = request.POST['lname']
        client.dob = request.POST['dob']
        client.email = request.POST['email']
        client.mobile_number =request.POST['pnumber']
        client.married_status = request.POST['mstatus']
        client.aadhaar_number = request.POST['anumber']
        client.pan_number = request.POST['pan']
        client.job = request.POST['job']
        client.qulification = request.POST['qualification']
        client.previous_policy = request.POST['ppolicy']
        client.previous_policy_number = request.POST['ppnumber']
        client.same_policy = request.POST['ppsame']
        client.agent_feedback = request.POST['agentf']
        client.campaign_feedback = request.POST['campaginf']
        campaign_id = request.POST.get('campagin')
        if campaign_id:
            client.campagin_id = campaign_id

        old = client.image
        new = request.FILES.get("file")
        if new:
            client.image = new
        else:
            client.image = old

        client.save()
        messages.success(request,'Edit Client Successfully')
        return redirect('view_client')

def delete_client(request,pk):
    data = ClientModel.objects.get(id=pk)
    data.delete()
    messages.success(request,'Delete Client Successfully')
    return redirect('view_client')