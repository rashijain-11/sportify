from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, UserProfileForm
from orders.models import Order

def signup_view(request):
    """
    Handles user registration and immediately signs the user in.
    """
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"🎉 Welcome to Sportify, {user.first_name or user.username}! Your athlete account is active.")
            return redirect('home')
        else:
            messages.error(request, "Please correct the errors in the signup form.")
    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    """
    Handles user authentication and login.
    """
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {user.first_name or user.username}!")
                next_url = request.GET.get('next', 'home')
                return redirect(next_url)
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    """
    Logs out user and redirects to homepage.
    """
    logout(request)
    messages.info(request, "You have been logged out of Sportify.")
    return redirect('home')


@login_required
def profile_view(request):
    """
    Displays athlete profile details, allows updating shipping address,
    and shows past orders and their status.
    """
    profile = request.user.profile
    orders = Order.objects.filter(user=request.user).prefetch_related('items').order_by('-created_at')

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your delivery address details have been updated.")
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)

    context = {
        'form': form,
        'orders': orders,
    }
    return render(request, 'accounts/profile.html', context)
