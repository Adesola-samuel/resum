from django.shortcuts import render, redirect
from .models import Message

def index(request):
    return render(request, 'index.html', {})

def folio(request):
    return render(request, 'portfolio-details.html', {})

def msg(request):
    if request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        t = Message(name = name,
                    email=email,
                    subject=subject,
                    message = message)
        t.save()
        return render(request, 'index.html', {'return_msg':'Your message has been sent. Thank you!'})
    return redirect("main:home")
