from django.contrib import admin
from .models import Student, Group, MonthJournal

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
	pass


admin.site.register(Student)
admin.site.register(Group)
admin.site.register(MonthJournal)