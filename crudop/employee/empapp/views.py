from django.shortcuts import render, redirect
from .forms import Signupform
from .forms import EmployeeForm
from .models import Employee
from django.contrib import messages, auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def show(request):
    # all_employees = Employee.objects.all()
    # return render(request, 'empapp/show.html', {'all_employees': all_employees})
    employees = Employee.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(employees, 5)
    try:
        all_employees = paginator.page(page)
    except PageNotAnInteger:
        all_employees = paginator.page(1)
    except EmptyPage:
        all_employees = paginator.page(paginator.num_pages)

    return render(request, 'empapp/show.html', { 'all_employees': all_employees })

def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('show')
            except:
                pass
        else:
            messages.add_message(request, messages.ERROR, 'Error please check the details ')
            return redirect('emp')
    else:
        form = EmployeeForm()
    return render(request, 'empapp/index.html', {'form': form})

def detail(request, emp_id):
    employee = Employee.objects.get(id=id)
    return render(request,'empapp/detail.html', {'employee':employee})

def update(request, pk):
    employee = Employee.objects.get(pk=pk)
    form = EmployeeForm(request.POST, instance=employee)

    if form.is_valid():
        form.save()
        return redirect('show')
    return render(request, 'empapp/edit.html', {'employee': employee})


def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'empapp/edit.html', {'employee': employee})

def delete(request, pk):
    employee = Employee.objects.get(pk=pk)
    employee.delete()
    return redirect('show')

def login(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('show')
        else:
            messages.add_message(request, messages.ERROR, 'Invalid User')
    return render(request, 'empapp/login.html')

def logout(request):
    auth.logout(request)
    return render(request, 'empapp/logout.html')

def signup(request):
    if request.method == 'POST':
        form = Signupform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = auth.authenticate(username=username, password=raw_password)
            auth.login(request, user)
            return redirect('login')
    else:
        form = Signupform()
    return render(request, 'empapp/signup.html', {'form': form})