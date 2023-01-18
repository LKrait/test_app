from django.contrib import admin
from . import models

class AcademicYearAdmin(admin.ModelAdmin):
	verbose_name = ['Academic Year']

admin.site.register(models.AcademicYear, AcademicYearAdmin)
admin.site.register(models.Term)
admin.site.register(models.Week)
admin.site.register(models.Subject)
