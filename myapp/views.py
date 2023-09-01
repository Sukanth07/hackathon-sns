from django.contrib.auth.decorators import login_required  # Import login_required decorator
from django.shortcuts import render, redirect
from .models import Users  # Import your Users model
from .forms import CLTForm, SCDForm, CFCForm, IIPCForm, SRIForm

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

def pillar_form(request):
    pillar = request.POST.get('pillar')
    print(pillar)
    
    return render(request, 'student.html', {'pillar': pillar})

def event_form_clt(request):
    if request.method == 'POST':
        form = CLTForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            return redirect('student',username=username)
        else:
            print(form.errors)  # Print form errors for debugging
    else:
        form = CLTForm()

    return render(request, 'student.html', {'form': form})

def event_form_scd(request):
    if request.method == 'POST':
        form = SCDForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            return redirect('student',username=username)
        else:
            print(form.errors)  # Print form errors for debugging
    else:
        form = SCDForm()

    return render(request, 'student.html', {'form': form})

def event_form_cfc(request):
    if request.method == 'POST':
        form = CFCForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            return redirect('student',username=username)
        else:
            print(form.errors)  # Print form errors for debugging
    else:
        form = CFCForm()

    return render(request, 'student.html', {'form': form})

def event_form_iipc(request):
    if request.method == 'POST':
        form = IIPCForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            return redirect('student',username=username)
        else:
            print(form.errors)  # Print form errors for debugging
    else:
        form = IIPCForm()

    return render(request, 'student.html', {'form': form})

def event_form_sri(request):
    if request.method == 'POST':
        form = SRIForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            return redirect('student',username=username)
        else:
            print(form.errors)  # Print form errors for debugging
    else:
        form = SRIForm()

    return render(request, 'student.html', {'form': form})

def view_activities(request):
    return render(request, "view_activities.html")