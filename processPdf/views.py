from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import UploadFileForm

# Create your views here.

def index(request):
    #return HttpResponse("Pdf goes here")
    #upload_file(request)
    if(request.method=='POST'):
        return upload_file(request)
    return render(request, 'processPdf/home.html')

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        print(form.is_valid(),"Is is??")
        if form.is_valid():
            a =handle_uploaded_file(request.FILES['file'])
            print("---a is ",a)
            #return HttpResponseRedirect('/success/url/')
            return HttpResponse("Successful!"+a)
    else:
        form = UploadFileForm()
    #return render(request, 'upload.html', {'form': form})
    return HttpResponse("Success!!")

def handle_uploaded_file(file1):
    print(type(file1),"hsga")
    x = file1.read()
    x= x.decode("utf-8")
    print('The file',x,type(x))
    
    return x
    # with open(file1) as file:
    #     text = file.read()
    #     print(text)
    #     return text


def save_pdf(pdf,filename):
    config = "--psm 4 --oem 1"
    #pdf = pytesseract.image_to_pdf_or_hocr("test.png",config=config,extension='pdf')
    with open(filename,"wb") as file:
        file.write(bytearray(pdf))
        file.close()



