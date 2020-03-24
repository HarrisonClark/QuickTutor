from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import TutorRequestForm
from .models import tutorRequest, Student


@login_required
def index(request):
    return render(request, 'study/index.html')


@login_required
def tutor_request(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TutorRequestForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            cour = form.cleaned_data['course']
            desc = form.cleaned_data['description']
            stud = Student.objects.filter(user=request.user)[0]

            newReq = tutorRequest(student=stud, course=cour, description=desc)
            newReq.save()

            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TutorRequestForm()

    return render(request, 'study/request.html', {'form': form})
