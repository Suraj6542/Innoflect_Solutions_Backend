from django.shortcuts import render
from .models import ContactMessage
from django.contrib import messages
def index(request):
    if request.method=='POST':
        Name=request.POST['Name']
        Email=request.POST['Email']
        Description=request.POST['Description']
        subject=request.POST['Subject']
        ContactMessage.objects.create(name=Name, email=Email, subject=subject, message=Description,)
        messages.success(request,'Data has been submitted')
        

    return render(request,'index.html')