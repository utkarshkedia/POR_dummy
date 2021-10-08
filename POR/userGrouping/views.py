from django.shortcuts import render,HttpResponse
from .decorators import allowed_users
# Create your views here.

def home(response):
    return render(response, "home.html", {"details":response.user.groups.all()})

@allowed_users(allowed_roles=["qual_engineer","admin"])
def home2(response):
    return HttpResponse("You are viewing home2")

#response.user.is_authenticated
#response.user.get("")
