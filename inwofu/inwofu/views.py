# views.py (Corrected)

from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from .models import ContactMessage, Project
from django.contrib import messages

def project_detail_view(request, project_slug):
    # This view is for the detail page and is correct
    project = get_object_or_404(Project, slug=project_slug)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)

def home(request):
    # 1. ADD THIS LINE BACK to get projects for the carousel
    projects = Project.objects.all()
    
    # 2. Handle the form submission
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent!')
            return redirect('/#contact') 
    else:
        # For a GET request, create an empty form
        form = ContactForm()

    # 3. ADD 'projects' back to the context dictionary
    context = {
        'projects': projects,
        'form': form,
    }
    
    # 4. Pass the full context to the template
    return render(request, 'index.html', context)