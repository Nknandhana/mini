from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from .models import User,Subject

from django.core.files.storage import FileSystemStorage

# Signup View
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        phone = request.POST['phone']
        gender = request.POST['gender']
        academic_year = request.POST['academic_year']

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


    

def index(request):
    return render(request, 'my_app/upload.html')

def index(request):
    return render(request, 'my_app/internal_marks.html')

def profile(request):
    if request.method == 'POST':
        user = request.user
        user.name = request.POST.get('name')
        user.email = request.POST.get('email')
        if 'profile_image' in request.FILES:
            user.profile_image = request.FILES['profile_image']
        user.save()
        return redirect('profile')  # Redirect to avoid resubmission on refresh
    return render(request, 'profile.html', {'user': request.user})




def register_subject(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    # Register logic here, like creating a student record
    # This is just a placeholder to show how the subject registration works
    return render(request, 'registration_success.html', {'subject': subject})

# View to display marks and allow faculty to upload marks

def view_marks(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    students = Student.objects.filter(subject=subject)
    
    if request.method == 'POST':
        student_id = request.POST['student_id']
        marks = Marks.objects.get(student_id=student_id)
        
        # Update marks
        marks.exam_1 = int(request.POST['exam_1'])
        marks.exam_2 = int(request.POST['exam_2'])
        marks.exam_3 = int(request.POST['exam_3'])
        marks.exam_4 = int(request.POST['exam_4'])
        marks.save()
        
        return redirect('view_marks', subject_id=subject_id)

    return render(request, 'view_marks.html', {'subject': subject, 'students': students})

def faculty_home(request):
    # Your view logic here
    return render(request, 'faculty_home.html')

def faculty_home(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        note = Note.objects.create(title=title, content=content, uploaded_by=request.user)
        return JsonResponse({'status': 'success'})
    
    notes = Note.objects.all()
    return render(request, 'faculty_home.html', {'notes': notes})

def student_home(request):
    notes = Note.objects.all()
    return render(request, 'student_home.html', {'notes': notes})


def upload_notes(request):
    if request.method == 'POST':
        # Handle the form submission to upload notes
        title = request.POST.get('title')
        content = request.POST.get('content')
        note = Note.objects.create(title=title, content=content, uploaded_by=request.user)
        return render(request, 'upload_success.html')  # or redirect to another page
    return render(request, 'upload_notes.html') 

def upload_note_view(request):
    if request.method == 'POST':
        form = NoteUploadForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.faculty = request.user  # Assign the logged-in user as the faculty
            note.save()
            return render(request, 'upload_note.html', {'form': form, 'success': True})
    else:
        form = NoteUploadForm()

    notes = Note.objects.filter(faculty=request.user)  # Show only notes uploaded by the logged-in faculty
    return render(request, 'upload_note.html', {'form': form, 'notes': notes, 'success': False})

