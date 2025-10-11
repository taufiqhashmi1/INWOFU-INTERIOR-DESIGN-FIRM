from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone # Import timezone
import uuid # Import for unique slugs

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"

class Project(models.Model):
    # --- Re-introduced useful fields ---
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, max_length=255)
    thumbnail = models.ImageField(
        upload_to='projects/thumbnails/', 
        help_text="Image shown on the homepage carousel.", 
        blank=True, 
        null=True
    )
    short_description = models.CharField(
        max_length=255, 
        help_text="A brief teaser shown on the project card.", 
        blank=True
    )
    full_description = models.TextField(blank=True)
    client = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    
    # --- FIXED date_created field ---
    date_created = models.DateField(auto_now_add=True)
    year = models.IntegerField(blank=True, null=True, help_text="Year the project was completed.")

    class Meta:
        ordering = ['-date_created']

    # --- IMPROVED save method for robust, unique slugs ---
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            unique_slug = base_slug
            # Check if a project with this slug already exists
            while Project.objects.filter(slug=unique_slug).exists():
                # If it exists, append a short unique ID
                unique_slug = f'{base_slug}-{uuid.uuid4().hex[:4]}'
            self.slug = unique_slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'project_slug': self.slug})


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects/gallery/')
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Image for {self.project.title}"