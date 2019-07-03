from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import UploadFileForm

# Create your views here.

def index(request):
    #return HttpResponse("Pdf goes here")
    return render(request, 'processPdf/home.html')

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def handle_uploaded_file(file1):
    pass
