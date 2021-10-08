from django.shortcuts import render,redirect,response
from django.core.mail import send_mail
from django.contrib.auth.models import Group,User

# Create your views here.
def mail(response):
    if response.user.is_authenticated:
        user_email = []
        current_user = response.user.username
        if response.user.is_superuser:
            pass
        else:
            user_email.append(response.user.email)

        admin_group = Group.objects.get(name='admin')
        admin_users = admin_group.user_set.all()
        admin_emails = []
        for admin_user in admin_users:
            admin_emails.append(admin_user.email)

        recepient_emails = user_email + admin_emails
        print(recepient_emails)
        send_mail(
            "Modified",
            current_user + " made changes",
            "ukedia@nvidia.com",
            recepient_emails,
            auth_user = "ukedia@nvidia.com",
            auth_password = "Ready2wrk@NVIDIA")
        return redirect('/')
    else:
        return ('/')