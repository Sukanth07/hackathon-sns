from django.shortcuts import render, redirect
from .models import Users  # Import your Users model

def home(request):
    return render(request,"home.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = Users.objects.get(username=username, password=password)
            if user.designation == 'Student':
                return redirect('student', username=user.username)  # Redirect to student.html
            elif user.designation == 'Faculty':
                return redirect('home')  # Redirect to faculty.html
        except Users.DoesNotExist:
            pass  # User credentials are not valid

        error_message = 'Invalid Credentials'
        return render(request, "login.html", {'error_message': error_message})

    return render(request, "login.html")

def student(request, username):
    user = Users.objects.get(username=username)
    mydict = {
        'stud_fullname':user.fullname,
        'stud_dept':user.dept,
        'stud_reg':user.username,
        'stud_batch':f"({(int(user.graduation)-4)} - {int(user.graduation)})"
    }
    print(mydict)
    return render(request, "student.html", mydict)