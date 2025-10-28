from django.contrib import admin
from .models import Project, ProjectImage

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')
    search_fields = ('title', 'user__username')
    list_filter = ('created_at',)
    fieldsets = (
        ('Інформація про проеєкт', {
            'fields': ('user', 'title', 'desc')
        }),
        ('Фали та зображення', {
            'fields': ('link', 'file')
        })
    )


admin.site.register(ProjectImage)