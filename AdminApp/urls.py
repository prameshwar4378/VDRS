from django.contrib import admin
from django.urls import path 
from . views import *
urlpatterns = [ 
    path('', dashboard, name='admin_dashboard'),
    path('vehicle_list/', vehicle_list, name='admin_vehicle_list'),
    path('admin_individual_dashboard/', admin_individual_dashboard, name='admin_individual_dashboard'),
    path('admin_reports/', admin_reports, name='admin_admin_reports'),
    path('admin_activity_logs/', admin_activity_logs, name='admin_activity_logs'),

]
