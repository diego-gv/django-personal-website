from django.shortcuts import render, redirect


# Create your views here.
def dashboard(request):
    # if the user is not authenticated cannot see the control panel
    if not request.user.is_authenticated:
        return redirect('index')
    
    return render(request, "users/dashboard.html")
