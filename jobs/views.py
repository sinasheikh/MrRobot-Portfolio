from django.shortcuts import render
from .models import Job


# Create your views here.
def elliot(request):
    jobs_objects = Job.objects.all()
    return render(request, 'jobs/elliot.html', {'jobs_list': jobs_objects})
