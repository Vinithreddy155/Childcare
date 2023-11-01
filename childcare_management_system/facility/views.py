from django.shortcuts import render
from .models import UserProfile
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create a user profile and assign a role (for simplicity, everyone is a parent now)
            UserProfile.objects.create(user=user, role='PARENT')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

from django.contrib.auth import authenticate, login

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            # Fetch the user profile to determine role
            profile = UserProfile.objects.get(user=user)
            
            # Redirect based on role
            if profile.role == 'SYS_ADMIN':
                return redirect('sys_admin_dashboard')
            
            elif profile.role == 'FAC_ADMIN':
                return redirect('fac_admin_dashboard')
            
            # Similarly, you can add other roles here:
            elif profile.role == 'TEACHER':
                return redirect('teacher_dashboard')
            elif profile.role == 'PARENT':
                return redirect('parent_dashboard')
            
            # If no specific role dashboard is found, redirect to some default view
            return redirect('default_view')
        
        else:
            # If authentication fails, return an error message
            return render(request, 'registration/login.html', {'error': 'Invalid username or password'})
    
    # If the request is not POST (i.e., GET), render the login page
    return render(request, 'registration/login.html')


@login_required
def sys_admin_dashboard(request):
    # Assuming there's a 'sys_admin_dashboard.html' template for the system administrator dashboard
    return render(request, 'sys_admin_dashboard.html')

@login_required
def fac_admin_dashboard(request):
    # Assuming there's a 'fac_admin_dashboard.html' template for the facility administrator dashboard
    return render(request, 'fac_admin_dashboard.html')

from django.shortcuts import render, redirect
from .forms import FacilityForm
from .models import Facility

def manage_facility(request, facility_id=None):
    if facility_id:
        instance = Facility.objects.get(id=facility_id)
    else:
        instance = None

    if request.method == 'POST':
        form = FacilityForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('fac_admin_dashboard')  # or any other success page
    else:
        form = FacilityForm(instance=instance)

    context = {'form': form}
    return render(request, 'manage_facility.html', context)

def landing_page(request):
    return render(request, 'landing_page.html')