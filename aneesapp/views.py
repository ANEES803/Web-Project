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

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            subject = form.cleaned_data['subject']
            sender_email = form.cleaned_data['email']
            message = f"From: {form.cleaned_data['name']} ({sender_email})\n\n{form.cleaned_data['message']}"

            try:
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.CONTACT_EMAIL],
                    fail_silently=False,
                )
            except Exception as e:
                print("Email error:", e)
                messages.error(request, f"Could not send email: {str(e)}")

            messages.success(request, 'Your message has been sent successfully!')
            return redirect('/contact/')  # Hardcoded path to avoid NoReverseMatch
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
