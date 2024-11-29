from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404
from app.models import Phones
# Create your views here.


def home(request):
    phn = Phones.objects.all()
    return render(request, 'index.html' , {'phn':phn})

def detail(request,id):
    phone = Phones.objects.get(id=id)
    return render(request,'detail.html', {'phone':phone})

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

        # return HttpResponse('Successfully Saved')
        return HttpResponseRedirect('/')

def edit_info(request, id):
    Info_update = get_object_or_404(Phones, id=id)

    if request.method == "POST" :
        b = request.POST['brand']
        s = request.POST['storage']
        c = request.POST['camera']
        bt = request.POST['battery']
        d = request.POST['display']
        p = request.POST['price']

        # Update student details
        Info_update.brand = b
        Info_update.storage = s
        Info_update.camera = c
        Info_update.battery = bt
        Info_update.display = d
        Info_update.price = p

        # Redirect back to home page
        return HttpResponseRedirect('/')
    # Render the form pre-filled with the student's data
    return render(request, 'listpage.html', {"Info_update": Info_update})

def detlet_phone(request,id):
    phn = Phones.objects.get(id=id)
    phn.delete() 
    return HttpResponseRedirect('/')
