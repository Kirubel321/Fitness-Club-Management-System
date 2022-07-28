from django.contrib import admin
from .models import PackageList, PlanList, TrainerList, MemberList

# Register my models here.

admin.site.register(PackageList)
admin.site.register(PlanList)
admin.site.register(TrainerList)
admin.site.register(MemberList)