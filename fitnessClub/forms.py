from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import MemberList, TrainerList, PackageList, PlanList


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class MemberListForm(ModelForm):
    class Meta:
        model = MemberList
        fields = '__all__'

class PackageListForm(ModelForm):
    class Meta:
        model = PackageList
        fields = '__all__'

class PlanListForm(ModelForm):
    class Meta:
        model = PlanList
        fields = '__all__'

class TrainerListForm(ModelForm):
    class Meta:
        model = TrainerList
        fields = '__all__'