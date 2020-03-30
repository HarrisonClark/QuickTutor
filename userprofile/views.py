from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .forms import EditProfile

@login_required
def index(request):
    return render(request, 'userprofile/index.html')

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfile(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('userprofile:index'))
    else:
        form = EditProfile(instance=request.user)
        args = {'form': form}
        return render(request, 'userprofile/edit.html', args)