from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, authenticate
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import Student, Subject
from .forms import StudentForm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('students')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('students')
        else:
            error_message = 'Invalid credentials'
    else:
        error_message = ''
    return render(request, 'login.html', {'error_message': error_message})


@login_required
def stud_list(request):
    query = request.GET.get('search')
    if query:
        students = Student.objects.filter(
            Q(last_name__icontains=query) |
            Q(first_name__icontains=query)  # , user=request.user
        )
    else:
        # students = Student.objects.filter(user=request.user)#
        students = Student.objects.all()

    return render(request, 'students/students.html', {'students': students, 'query': query})


@ login_required
def stud_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            stud = form.save(commit=False)
            stud.user = request.user
            stud.save()
            return redirect('students')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form})


def stud_update(request, pk):
    todo = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = StudentForm(instance=todo)
    return render(request, 'students/student_form.html', {'form': form})


def stud_delete(request, pk):
    stud = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        stud.delete()
        return redirect('students')
    return render(request, 'students/student_confirm_delete.html', {'stud': stud})
