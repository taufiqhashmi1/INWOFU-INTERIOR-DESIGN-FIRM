from django.contrib import admin
from .models import ContactMessage,Project, ProjectImage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')  # Optional: shows these fields in admin list
    search_fields = ('name', 'email', 'message')      # Optional: adds a search box

# This allows you to add/edit gallery images directly on the Project page
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1  # How many extra empty image slots to show

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    # Controls how the list of all projects is displayed
    list_display = ('title', 'client', 'location', 'year')
    
    # Automatically creates the slug from the title as you type
    prepopulated_fields = {'slug': ('title',)}
    
    # This is where we nest the gallery images
    inlines = [ProjectImageInline]

# Note: We don't need a separate admin.site.register(ProjectImage)
# because it's already handled by the inline above.
