from django.contrib import admin
from .models import Job, Employee, Genero



class JobAdmin(admin.ModelAdmin):
    list_display=('id','name')

class GeneroAdmin(admin.ModelAdmin):
    list_display=('id', 'sexo')

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('id','ci','name','last_name','phone','points','adress', 'gender', 'birth_date', 'job_id', 'is_active' )



admin.site.register(Job,JobAdmin)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Genero,GeneroAdmin)

# Register your models here.
