from django.shortcuts import render,redirect
from .models import Contact,NewsLetter
from .forms import ContactForm,NewsLetterForm
from django.contrib import messages


def index_view(request):
    return render(request,"website/index.html")

def about_view(request):
    return render(request,"website/about.html")

def contact_view(request):
    form=ContactForm(request.POST)
    
    if request.method=="POST":
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Your ticket has been sent.")
        else:
            messages.add_message(request, messages.ERROR, "Your message was not sent")

    return render(request,"website/contact.html",{'form': form})

def elements_view(request):
    return render(request,"website/elements.html")

def newsletter_view(request):
    form=NewsLetterForm(request.POST)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, "Your email has been successfully registered.")
    else:
        messages.add_message(request, messages.ERROR, "Your email was not registered. Please try again")
        
    return redirect(request.META['HTTP_REFERER'])


