from django.contrib import admin

# Register your models here.
from . models import Project,ProjectCategory,ProjectStats,Client

admin.site.register(Client)
admin.site.register(ProjectCategory)
admin.site.register(Project)
admin.site.register(ProjectStats)
