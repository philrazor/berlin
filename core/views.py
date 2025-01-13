from django.shortcuts import render ,get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Part
from .models import Make, CarModel
from django.shortcuts import render
from .forms import SearchForm

def home(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            # Process the form data
            brand = form.cleaned_data['brand']
            model = form.cleaned_data['model']
            year = form.cleaned_data['year']
            return redirect("home")
    else:
        form = SearchForm()
        parts = Part.objects.all().order_by('-created_at')[:8]
    
    return render(request, 'core/home.html', {'form': form ,"recent_parts": parts})
def search_results(request):
    return HttpResponse('searched')


def search_page(request):
    brands = Make.objects.all()  # Get all available brands
    models = CarModel.objects.all()  # Get all available models
    return render(request, 'core/home.html', {'brands': brands, 'models': models})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})



def logout_user(request):
    logout(request)
    return redirect('home')

def custom_logout(request):
    logout(request)
    return redirect('home')