from django.http import HttpResponse
from django.shortcuts import render
from .forms import UploadResumeForm


def ResumeUploadView(request):
    if request.method == 'POST':
        form = UploadResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('File submitted successfully')
    else:
        form = UploadResumeForm()
        context = {
            'form': form,
        }
    return render(request, 'blog/Uploadresume.html', context)
