from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from apps.product.models import Resume, Job
from apps.product.serializers import ResumeSerializer

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import JobForm, ResumeForm

def index(request):
    job = Job.objects.all()
    resume = Resume.objects.all

    return render(request, 'index.html', {'job':job, 'resume':resume})

def  job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'job_detail.html', {'job': job})

def  resume_detail(request, pk):
    resume = get_object_or_404(Resume, pk=pk)
    return render(request, 'resume_detail.html', {'resume':resume})

def job_new(request):
    form = JobForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.created_at = timezone.now()
        post.save()
        return redirect('/', pk=post.pk)
    else:
        form = JobForm()
    return render(request, 'job_new.html', {'form': form})

def resume_new(request):
    form = ResumeForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.created_at = timezone.now()
        post.save()
        return redirect('/', pk=post.pk)
    else:
        form = JobForm()
    return render(request, 'job_new.html', {'form': form})

def job_edit(request, pk):
    post = get_object_or_404(Job, pk=pk)
    if request.method == "POST":
        form = JobForm(request.POST, instance=post)
        if form.is_valid():
            post.title = request.POST['title']
            post.company = request.POST['company']
            post.description = request.POST['description']
            post.requirements = request.POST['requirements']
            post.author = request.user
            post.created_at = timezone.now()
            post.save()
            return redirect('/', pk=post.pk)
    else:
        form = JobForm(instance=post)
    return render(request, 'job_edit.html', {'form': form})

def resume_edit(request, pk):
    post = get_object_or_404(Job, pk=pk)
    if request.method == "POST":
        form = ResumeForm(request.POST, instance=post)
        if form.is_valid():
            post.name = request.POST['name']
            post.company = request.POST['company']
            post.description = request.POST['description']
            post.requirements = request.POST['requirements']
            post.author = request.user
            post.created_at = timezone.now()
            post.save()
            return redirect('/', pk=post.pk)
    else:
        form = JobForm(instance=post)
    return render(request, 'job_edit.html', {'form': form})

def job_delete(request, pk):
    news = Job.objects.get(pk=pk)
    news.delete()
    return redirect('/')

# Create your views here.

class ResumeViewSet(ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer


class JobViewSet(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = ResumeSerializer