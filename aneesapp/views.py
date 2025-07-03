from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.



def index(request):
    return render(request, 'index.html')
def portfolio_details(request):
    return render(request, 'portfolio-details.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('/#contact')
    else:
        form = ContactForm()
    
    return render(request, 'index.html', {'form': form})
