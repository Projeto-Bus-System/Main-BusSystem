from django.shortcuts import render, redirect
from accounts.forms import FormCreateStudent
from django.http import HttpResponse

def createStudent(request):
    if request.method == 'POST':
        form_student = FormCreateStudent(request.POST)
        if form_student.is_valid():
            form_student.save()
            return redirect('google.com')
        else:   
            return HttpResponse(status=500)
    else:
        form_student = FormCreateStudent()
        context = {
            'form_student':form_student
        }
    return render(request, 'crudStudent/create.html',context)