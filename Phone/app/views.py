from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from app.models import Phones
# Create your views here.


def home(request):
    phn = Phones.objects.all()
    return render(request, 'index.html' , {'phn':phn})

def Create(request):
    phn = Phones.objects.all()
    if request.method == 'GET':
        return render(request, 'listpage.html')

    else:
        request.method == "POST"
        b = request.POST['brand']
        s = request.POST['storage']
        c = request.POST['camera']
        bt = request.POST['battery']
        d = request.POST['display']
        p = request.POST['price']

        phn = Phones.objects.create(brand=b, storage=s, camera=c, battery=bt, display=d, price=p)

        phn.save()

        return HttpResponse('Successfully Saved')

