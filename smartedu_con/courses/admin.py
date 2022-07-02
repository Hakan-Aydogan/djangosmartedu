from django.contrib import admin
from .models import Course, Category, Tag

# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'available',
                    'teacher', 'date', 'student_count')
    list_display_links = ('id', 'name', 'available', 'teacher', 'date')
    list_filter = ('available',)
    search_fields = ('name', 'description', 'teacher',)

    def student_count(self, obj):
        return len(obj.students.all())
    student_count.short_description = 'students'

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).prefetch_related('students')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
