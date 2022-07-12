from django.shortcuts import render
from myapp.models import Contact

# Create your views here.
def index(request):
    return render(request, 'index.html')

def success(request):
    if (request.method == "POST"):
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        contact = Contact(name=name, phone=phone, email=email, password=password)
        contact.save()
        contactData = Contact.objects.all()
        context = {
            'data': contactData
        }
    return render(request, 'success.html', context)