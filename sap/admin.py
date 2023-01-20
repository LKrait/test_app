from django.contrib import admin
from . import models

class AcademicYearAdmin(admin.ModelAdmin):
	verbose_name = ['Academic Year']

admin.site.register(models.AcademicYear, AcademicYearAdmin)
admin.site.register(models.Term)
admin.site.register(models.Week)
admin.site.register(models.Subject)


#Configuring admin title
admin.site.site_header = "SAP"
admin.site.site_title = "SAP"
admin.site.index_title = "Welcome to SAP"
