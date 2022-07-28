

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create my models here.
class PlanList(models.Model):
    PLANS = (
        ('1Month','1Month'),
        ('3Month','3Month'),
        ('6Month','6Month'),
        ('12Month','12Month')
    )
    planName = models.CharField(max_length=50, null=True, choices = PLANS)
    amount = models.FloatField(null=True,blank=True)
    dateCreated = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.planName

class PackageList(models.Model):
    PACKAGE = (
        ('7 Day a Week','7 Day a Week'),
        ('3 Day a Week','3 Day a week')
    )
    packageName = models.CharField(max_length=50, null=True, choices = PACKAGE)
    amount = models.FloatField(null=True,blank=True)
    dateCreated = models.DateTimeField(auto_now_add=True, null=True)
    plan = models.ForeignKey(PlanList, on_delete=models.CASCADE)

    def __str__(self):
        return self.packageName

class TrainerList(models.Model):
    trainerName = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phoneNumber = PhoneNumberField(unique=True,null = True,blank = True)
    trainerImage = models.ImageField(blank=True)
    dateCreated = models.DateTimeField(auto_now_add=True, null=True)
    trainerImage = models.ImageField()
    
    def __str__(self):
        return self.trainerName

class MemberList(models.Model):
    STATUS = (
        ('Active','Active'),
        ('Inactive','Inactive')
    )
    G_CHOICES = (
        ('M','Male'),
        ('F','Female')
    )
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.CharField(max_length=50,null = True, blank= True)
    phoneNumber = PhoneNumberField(unique=True,null = True,blank = True)
    memberImage = models.ImageField()
    gender= models.CharField(max_length=1,choices=G_CHOICES)
    age = models.IntegerField()
    address = models.CharField(max_length=50)
    plan = models.ForeignKey(PlanList, on_delete=models.CASCADE)
    package = models.ForeignKey(PackageList, on_delete=models.CASCADE)
    trainer = models.ForeignKey(TrainerList, on_delete=models.CASCADE)
    dateCreated = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=50, null=True, choices=STATUS)

    def __str__(self):
        return self.firstName

