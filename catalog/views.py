from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'You have new message from {name}({email}): {message}')
    return render(request, 'catalog/index.html')

def home(request):
    return render(request, 'catalog/home.html')

def contact(request):
    return render(request, 'catalog/contact.html')

