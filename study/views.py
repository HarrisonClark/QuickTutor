from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import TutorRequestForm
from .models import tutorRequest, Student
from django.utils import timezone
from django.views import generic


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

            newReq = tutorRequest(student=stud, course=cour,
                                  description=desc, pub_date=timezone.now())
            newReq.save()

            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TutorRequestForm()

    return render(request, 'study/request.html', {'form': form})


class RequestsView(generic.ListView):
    template_name = "study/request_list.html"
    context_object_name = "requests_list"

    def get_queryset(self):
        """
        Return five most recent suggestions
        """
        return tutorRequest.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
