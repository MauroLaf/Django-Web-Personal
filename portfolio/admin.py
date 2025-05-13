from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Project, ProjectAdmin) #le pase la configuracion extendida pasandole la clase projectadmin como parametro para ver la edicion de campos
