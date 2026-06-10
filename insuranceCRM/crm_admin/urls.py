from django.urls import path
from crm_admin import views

urlpatterns =[
    path('Admin/Dashboard',views.admin_dashboard,name='admin_dashboard'),
    path('Add/Agent',views.add_agent,name='add_agent'),
    path('ADD/AGENT/DATA',views.addagent,name='addagent'),
    path('Edit/Agent/<int:pk>',views.edit_agent,name='edit_agent'),
    path('Edit/Agent/Data/<int:pk>',views.editagent,name='editagent'),
    path('Delete/Agent/Data/<int:pk>',views.delete_agent,name='delete_agent'),
    path('check/agent/data',views.check_agent_data,name='check_agent_data'),
    path('edit/agent/data',views.edit_agent_data,name='edit_agent_data'),
    path('View/Agent',views.view_agent,name='view_agent'),
    path('Add/campagin',views.add_campagin,name='add_campagin'),
    path('Add/Campagin/Data',views.addcampagin,name='addcampagin'),
    path('View/campagin',views.view_campagin,name='view_campagin'),
    path('Edit/Campagin/<int:pk>',views.edit_campagin,name='edit_campagin'),
    path('Edit/Campagin/Data/<int:pk>',views.editcampagin,name='editcampagin'),
    path('Delete/Campagin/<int:pk>',views.delete_campagin,name='delete_campagin'),
    path('View/Total/Client/',views.view_total_client,name='view_total_client'),

]