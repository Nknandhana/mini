from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.contrib.sessions.backends.db import SessionStore
from .models import User

# Signup View
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        phone = request.POST['phone']
        gender = request.POST['gender']

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')

        # Check if email or username already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered!")
            return redirect('signup')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken!")
            return redirect('signup')

        # Create new user
        hashed_password = make_password(password)
        user = User(username=username, email=email, password=hashed_password, phone=phone, gender=gender)
        user.save()

        messages.success(request, "Registration successful! Please log in.")
        return redirect('login')

    return render(request, 'signup.html')

# Login View
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Authenticate user
        try:
            user = User.objects.get(email=email)
            if check_password(password, user.password):
                # Set session
                request.session['user_id'] = user.id
                request.session['username'] = user.username
                messages.success(request, f"Welcome {user.username}!")
                return redirect('dashboard')  # Replace 'dashboard' with your desired redirect URL
            else:
                messages.error(request, "Invalid credentials!")
        except User.DoesNotExist:
            messages.error(request, "User does not exist!")

    return render(request, 'login.html')

# Logout View
def logout(request):
    request.session.flush()
    messages.success(request, "You have been logged out!")
    return redirect('login')
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.contrib.sessions.backends.db import SessionStore
from .models import User

# Signup View
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        phone = request.POST['phone']
        gender = request.POST['gender']

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')

        # Check if email or username already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered!")
            return redirect('signup')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken!")
            return redirect('signup')

        # Create new user
        hashed_password = make_password(password)
        user = User(username=username, email=email, password=hashed_password, phone=phone, gender=gender)
        user.save()

        messages.success(request, "Registration successful! Please log in.")
        return redirect('login')

    return render(request, 'signup.html')

# Login View
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Authenticate user
        try:
            user = User.objects.get(email=email)
            if check_password(password, user.password):
                # Set session
                request.session['user_id'] = user.id
                request.session['username'] = user.username
                messages.success(request, f"Welcome {user.username}!")
                return render(request, 'welcome.html')  # Replace 'dashboard' with your desired redirect URL
            else:
                messages.error(request, "Invalid credentials!")
        except User.DoesNotExist:
            messages.error(request, "User does not exist!")

    return render(request, 'login.html')

# Logout View
def logout(request):
    request.session.flush()
    messages.success(request, "You have been logged out!")
    return redirect('login')
