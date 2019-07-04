from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UploadFileForm
import pytesseract
import os
pytesseract.pytesseract.tesseract_cmd = r'A:\Tools\tesseract-ocr\tesseract'
# Create your views here.


def index(request):
    h = []
    if(request.method == 'POST'):
        h = upload_file(request)
    return render(request, 'processPdf/home.html', {'content': h})


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        print(form.is_valid(), "Is is??")
        if form.is_valid():
            a = handle_uploaded_file(request.FILES['file'])
            print("---a is ", a)
            return a
            # return render(request, 'processPdf/home.html',{'content': a})
    else:
        form = UploadFileForm()
    # return render(request, 'upload.html', {'form': form})
    return "Failure"


def handle_uploaded_file(file1):
    print(type(file1), "hsga")
    #x = file1.read()
    #x= x.decode("utf-8")
    with open("media/"+file1.name, 'wb+') as f:
        for chunk in file1.chunks():
            f.write(chunk)
        f.close()
    filepath = "media/"+file1.name
    print(f.name, "the file is this", filepath)
    x = pytesseract.image_to_string(filepath)
    os.remove(filepath)
    #x = file1.name
    print('The text', x, type(x))
    x = x.split('\n')
    print("The List is ", x)
    return x


def save_pdf(pdf, filename):
    config = "--psm 4 --oem 1"
    #pdf = pytesseract.image_to_pdf_or_hocr("test.png",config=config,extension='pdf')
    with open(filename, "wb") as file:
        file.write(bytearray(pdf))

        file.close()
