from django.shortcuts import render
from .models import AuditLog
from users.decorators import admin_required
from django.contrib.admin.views.decorators import staff_member_required
from users.decorators import admin_or_officer_required

def audit_log_view(request):
    logs = AuditLog.objects.all().order_by('-timestamp')
    return render(request, 'audit/audit_logs.html', {'logs': logs})

@admin_required
def view_audit_logs(request):
    return render(request, 'audit/audit_logs.html')

@staff_member_required
def audit_log_view(request):
    logs = AuditLog.objects.all().order_by('-timestamp')  # You can filter/log based on role if needed
    return render(request, 'audit/logs.html', {'logs': logs})

@admin_or_officer_required
def audit_log_view(request):
    logs = AuditLog.objects.all().order_by('-timestamp')
    return render(request, 'audit/audit_logs.html', {'logs': logs})