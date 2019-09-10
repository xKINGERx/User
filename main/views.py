from django.shortcuts import render, redirect
from .models import User
from .models import User
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your view here.

def home(request):
    all_user = User.objects
    return render(request, 'main.html', {'all_user': all_user})

@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['First_name'] and request.POST['Last_name'] and request.FILES['Your_pic'] and request.POST['Your_details']:
            product = User()
            product.First_name = request.POST['First_name']
            product.Last_name = request.POST['Last_name']
            product.Your_details = request.POST['Your_details']
            product.Your_pic = request.FILES['Your_pic']
            product.save()
            return redirect('main')
        else:
            return render(request, create.html, {'error':'Please fill all the fields'})
    else:
        return render(request, 'create.html')
