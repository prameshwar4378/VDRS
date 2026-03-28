from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'admin_dashboard.html')

def vehicle_list(request):
    return render(request, 'admin_vehicle_list.html')


def admin_individual_dashboard(request):
    return render(request, 'admin_individual_dashboard.html')

def admin_reports(request):
    return render(request, 'admin_reports.html')

def admin_activity_logs(request):
    return render(request, 'admin_activity_logs.html')