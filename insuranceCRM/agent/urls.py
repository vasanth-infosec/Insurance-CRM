from django.urls import path
from agent import views

urlpatterns =[
    path('AGENT/Dashboard',views.agent_dashboard,name='agent_dashboard'),
    path('Update/Agent/Profile',views.update_agent,name='update_agent'),
    path('Update/Agent/Profile/Data',views.updateagent,name='updateagent'),
    path('check/agent/profile',views.check_agent_profile,name='check_agent_profile'),
    path('Change/Password/',views.change_password,name='change_password'),
    path('Change/Password/Data',views.changepassword,name='changepassword'),
    path('View/Agent/Campagin/',views.view_agent_campagin,name='view_agent_campagin'),
    path('Add/Client/',views.add_client,name='add_client'),
    path('Add/Client/DATA',views.addclient,name='addclient'),
    path('check/client/data',views.check_client_data,name='check_client_data'),
    path('check/edit/client/data',views.check_edit_client_data,name='check_edit_client_data'),
    path('View/Agent/Client',views.view_client,name='view_client'),
    path('Edit/Client/<int:pk>',views.edit_client,name='edit_client'),
    path('Edit/Client/Data/<int:pk>',views.editclient,name='editclient'),
    path('Delete/Client/<int:pk>',views.delete_client,name='delete_client'),
    
]