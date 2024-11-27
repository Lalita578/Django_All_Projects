

from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, HttpResponse
from app.models import Student

# Display all students
def home(request):
    stud = Student.objects.all()
    return render(request, 'Indexpage.html', {'stud': stud})

def detail(request,id):
    student = Student.objects.get(id = id)
    return render(request, 'detail.html', {'student':student})

def New_student(request):
    # st = Student.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'st_form.html')

    else:
        request.method == "POST"
        n = request.POST['name']
        a = request.POST['address']
        p = request.POST['phone_no']

        stud = Student.objects.create(name=n, address=a, phone_no=p)
        stud.save()

        return HttpResponse('Successfully Saved')



def edit_info(request, id):
    Info_update = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        n = request.POST['name']
        a = request.POST['address']
        p = request.POST['phone_no']

        # Update student details
        Info_update.name = n
        Info_update.address = a
        Info_update.phone_no = p
        Info_update.save()

        # Redirect back to home page
        return HttpResponseRedirect('/')

    # Render the form pre-filled with the student's data
    return render(request, 'st_form.html', {"Info_update": Info_update})


def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()  
    return HttpResponseRedirect('/')