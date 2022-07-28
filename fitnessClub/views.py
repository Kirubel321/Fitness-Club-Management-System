from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Count, Q

# Create your views here.
from .models import MemberList, TrainerList, PackageList, PlanList
from .forms import CreateUserForm, MemberListForm, PackageListForm, TrainerListForm, PlanListForm
from .filters import MemberListFilter


def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user )
                return redirect('login')
        context = {'form':form}
        return render(request, 'register.html',context)

def loginPage(request): 
    if request.method == 'POST':
        usern = request.POST.get('username')
        passwd = request.POST.get('password')
        user = authenticate(request, username=usern, password=passwd)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username OR passeword is incorrect')
            
    context = {}
    return render(request, 'login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def index(request):
    dataset= MemberList.objects.values('status').annotate(male_count=Count('status', filter=Q(gender='M')),
    female_count=Count('status', filter=Q(gender='F'))).order_by('status')

    # dataset2= PackageList.objects.values('plan').annotate(day7_count=Count('plan', filter=Q(package='7 day a week')),
    # day3_count=Count('plan', filter=Q(package='3 day a week'))).order_by('plan')


    count1 = MemberList.objects.all().count()
    count2 = MemberList.objects.filter(status = 'Active').count()
    context = {'count1':count1,'count2':count2, 'dataset':dataset}


    return render(request, 'index.html', context)


@login_required(login_url='login')
def members(request):

    form = MemberListForm()
    member = MemberList.objects.all()

    myFilter = MemberListFilter(request.GET, queryset=member)
    member = myFilter.qs

    if request.method == 'POST':
        form = MemberListForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()            
            messages.success(request, 'Members information is successfully added ')
            form = MemberListForm()
    context =  {'form':form,'member':member,'myFilter':myFilter}
    return render(request, 'members.html', context)



@login_required(login_url='login')
def updateMembers(request,pk):
    member = MemberList.objects.get(id=pk)
    form = MemberListForm(instance=member)
    if request.method == 'POST':
        form = MemberListForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, 'Members information is successfully updated ' )
            form = MemberListForm()
            return redirect('members')
    context={'form':form}
    return render(request, 'members.html', context)

@login_required(login_url='login')
def membersDetailView(request, pk):
    member = MemberList.objects.get(id=pk)
    context = {'member':member}
    return render(request, 'membersDetailView.html', context)

@login_required(login_url='login')
def trainerDetailView(request, pk):
    trainer = TrainerList.objects.get(id=pk)
    context = {'trainer':trainer}
    return render(request, 'TrainerDetailView.html', context)

@login_required(login_url='login')
def membershipvalidation(request):
    members = MemberList.objects.filter(status='Active')
    context = {'member':members}
    return render(request, 'membershipvalidation.html',context)

@login_required(login_url='login')
def packages(request):
    form = PackageListForm()
    package = PackageList.objects.all()
    if request.method == 'POST':
        form = PackageListForm(request.POST)
        if form.is_valid():
            form.save()            
            messages.success(request, 'Package information is successfully added ' )
            form = PackageListForm()
    context ={'form':form,'package':package}
    return render(request, 'packages.html', context)

@login_required(login_url='login')
def updatePackages(request,pk):
    package = PackageList.objects.get(id=pk)
    form = PackageListForm(instance = package)
    if request.method == 'POST':
        form = PackageListForm(request.POST, instance = package)
        if form.is_valid():
            form.save()            
            messages.success(request, 'Package information is successfully updated ' )
            form = PackageListForm()
            return redirect('packages')
    context = {'form':form}
    return render(request, 'packages.html',context)


@login_required(login_url='login')
def plans(request):
    form = PlanListForm()
    plan = PlanList.objects.all()
    if request.method == 'POST':
        form = PlanListForm(request.POST)
        if form.is_valid():
            form.save()           
            messages.success(request, 'Plans information is successfully added ' )
            form = PlanListForm()
    context = {'form':form,'plan':plan}
    return render(request, 'plans.html', context)

@login_required(login_url='login')
def updatePlans(request,pk):
    plan = PlanList.objects.get(id=pk)
    form = PlanListForm(instance = plan)
    if request.method == 'POST':
        form = PlanListForm(request.POST, instance = plan)
        if form.is_valid():
            form.save()           
            messages.success(request, 'Plans information is successfully updated ' )
            form = PlanListForm
            return redirect('plans')
    context = {'form':form}
    return render(request, 'plans.html',context)


@login_required(login_url='login')
def trainers(request):
    form = TrainerListForm()
    trainer =TrainerList.objects.all()
    if request.method == 'POST':
        form = TrainerListForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()          
            messages.success(request, 'Trainer information is successfully added ' )
            form = TrainerListForm()
    context = {'form':form,'trainer':trainer}
    return render(request, 'trainers.html', context)

@login_required(login_url='login')
def updateTrainers(request,pk):
    trainer = TrainerList.objects.get(id=pk)
    form = TrainerListForm(instance = trainer)
    if request.method == 'POST':
        form = TrainerListForm(request.POST, instance = trainer)
        if form.is_valid():
            form.save()            
            messages.success(request, 'Trainers information is successfully updated ' )
            form = TrainerListForm
            return redirect('trainers')
    context = {'form':form}
    return render(request, 'trainers.html',context)

@login_required(login_url='login')
def deleteMembers(request,pk):
    member = MemberList.objects.get(id=pk)
    if request.method == 'POST':
        member.delete()
        return redirect('members')
    context = {'item':member}
    return render(request, 'deleteMembers.html', context)

@login_required(login_url='login')
def deletePackages(request,pk):
    package = PackageList.objects.get(id=pk)
    if request.method == 'POST':
        package.delete()
        return redirect('packages')
    context = {'item':package}
    return render(request, 'deletePackages.html', context)


@login_required(login_url='login')
def deletePlans(request,pk):
    plan = PlanList.objects.get(id=pk)
    if request.method == 'POST':
        plan.delete()
        return redirect('plans')
    context = {'item':plan}
    return render(request, 'deletePlans.html', context)


@login_required(login_url='login')
def deleteTrainers(request,pk):
    trainer = TrainerList.objects.get(id=pk)
    if request.method == 'POST':
        trainer.delete()
        return redirect('trainers')
    context = {'item':trainer}
    return render(request, 'deleteTrainers.html', context)

