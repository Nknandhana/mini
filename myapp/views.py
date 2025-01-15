from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.contrib.sessions.backends.db import SessionStore
from .models import User
from django.http import HttpResponse





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
        user = User(username=username, email=email, password=hashed_password, phone=phone, gender=gender , acedemic_year=academic_year )
        user.save()

        messages.success(request, "Registration successful! Please log in.")
        return redirect('login')

    return render(request, 'signup.html')

# Login View
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        academic_year = request.POST.get('academic_year')
        role = request.POST.get('role')
        semester = request.POST.get('semester')

        # Authenticate user
        try:
            user = User.objects.get(email=email)
            if check_password(password, user.password):
                # Set session
                request.session['user_id'] = user.id
                request.session['username'] = user.username
                request.session['academic_year'] = academic_year
                request.session['role'] = role
                request.session['semester'] = semester
                messages.success(request, f"Welcome {user.username}!")
                return redirect('welcome')  # Replace 'dashboard' with your desired redirect URL
            else:
                messages.error(request, "Invalid credentials!")
        except User.DoesNotExist:
            messages.error(request, "User does not exist!")

    return render(request, 'login.html')

# welcome view
def welcome_view(request):
    return render(request, 'welcome.html')

# Logout View
def logout(request):
    request.session.flush()
    messages.success(request, "You have been logged out!")
    return redirect('login')


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

# # Login View
# def login(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']

#         # Authenticate user
#         try:
#             user = User.objects.get(email=email)
#             if check_password(password, user.password):
#                 # Set session
#                 request.session['user_id'] = user.id
#                 request.session['username'] = user.username
#                 messages.success(request, f"Welcome {user.username}!")
#                 return render(request, 'welcome.html')  # Replace 'dashboard' with your desired redirect URL
#             else:
#                 messages.error(request, "Invalid credentials!")
#         except User.DoesNotExist:
#             messages.error(request, "User does not exist!")

#     return render(request, 'login.html')

# Logout View
def logout(request):
    request.session.flush()
    messages.success(request, "You have been logged out!")
    return redirect('login')


def user_list(request):
    users = User.objects.all()  # Fetch all users from the database
    return render(request, 'user_list.html', {'users': users})

def internal_marks(request):
    # Your logic here
    return render(request, 'internal_marks.html')

def messages_view(request):
    # Logic to retrieve and display messages
    return render(request, 'messages.html')

def upload_notes(request):
    if request.method == 'POST' and request.FILES['notes']:
        notes_file = request.FILES['notes']
        fs = FileSystemStorage()
        filename = fs.save(notes_file.name, notes_file)
        # You can do something with the filename if you need
        return redirect('upload_success')  # Redirect to a success page after upload
    
    return render(request, 'upload_page.html')

def upload_seminar_assignment(request):
    if request.method == 'POST':
        seminar_file = request.FILES.get('seminar')
        assignment_file = request.FILES.get('assignment')
        fs = FileSystemStorage()
        
        seminar_filename = fs.save(seminar_file.name, seminar_file)
        assignment_filename = fs.save(assignment_file.name, assignment_file)
        
        # You can do something with the filenames if you need
        return redirect('upload_success')  # Redirect to success page after upload
    
    return render(request, 'upload_page.html')

def update_student_details(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        register_number = request.POST.get('register_number')
        subject = request.POST.get('subject')
        
        # Process the data, save it to the database, or whatever is needed
        # Assuming you have a Student model for saving the data
        # student = Student.objects.create(name=name, register_number=register_number, subject=subject)
        
        return redirect('update_success')  # Redirect after successfully updating details

    def messages_view(request):
      return render(request, 'messages.html')
    


def internal_marks(request):
    # Ensure the user is authenticated and has the correct role
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login if user is not authenticated
    
    role = getattr(request.user, 'role', None)  # Get the user's role (faculty, student, etc.)
    
    # Fetch all marks
    marks = Marks.objects.all()

    # Preprocess the marks to calculate average and total marks
    processed_marks = []
    for mark in marks:
        # Assuming sub1, sub2, sub3, sub4 are exam scores
        subject_marks = [mark.sub1, mark.sub2, mark.sub3, mark.sub4]
        subject_marks.sort(reverse=True)  # Sort the marks in descending order

        # Calculate the average (highest 2 out of 4 marks)
        average_mark = sum(subject_marks[:2]) / 2

        # Calculate the total marks (subject marks + lab)
        total_marks = sum(subject_marks) + mark.lab

        # Append processed mark data for use in the template
        processed_marks.append({
            'student': mark.student,
            'register_number': mark.student.register_number,
            'sub1': mark.sub1,
            'sub2': mark.sub2,
            'sub3': mark.sub3,
            'sub4': mark.sub4,
            'lab': mark.lab,
            'average_mark': average_mark,
            'total_marks': total_marks,
        })

    # Return the context to the template with role and processed marks
    return render(request, 'internal_marks.html', {'role': role, 'marks': processed_marks})