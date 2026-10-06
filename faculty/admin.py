from django.contrib import admin

from .models import Department, Program, SiteContent, Teacher


@admin.register(SiteContent)
class SiteContentAdmin(admin.ModelAdmin):
    list_display = ("title",)

    def has_add_permission(self, request):
        
        return not SiteContent.objects.exists()


class TeacherInline(admin.TabularInline):
    model = Teacher
    extra = 1


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "head")
    search_fields = ("name", "head")
    inlines = [TeacherInline]


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "department", "coordinator_name")
    list_filter = ("department",)
    search_fields = ("name", "code")


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "degree", "department")
    list_filter = ("department",)
    search_fields = ("name",)
