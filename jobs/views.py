from django.shortcuts import render

# Create your views here.
def elliot(request ):
    return render(request, 'jobs/elliot.html')
