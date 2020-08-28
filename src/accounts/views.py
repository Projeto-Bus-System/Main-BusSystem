from django.shortcuts import render, redirect
from accounts.forms import FormCreateStudent, FromCreateUser
from django.http import HttpResponse

def createStudent(request):
    if request.method == 'POST':

        form_student = FormCreateStudent(request.POST)
        form_user = FromCreateUser(request.POST)


        if form_student.is_valid() & form_user.is_valid():


            try:
                form_student.save(commit=False)
            except:
                return HttpResponse(status=501)


            try:
                form_user.save(commit=False)
            except:
                return HttpResponse(status=501)

                
            form_student.save()
            form_user.save()
            return HttpResponse(status=200)
        else:   
            return HttpResponse(status=500)

    elif request.method == 'GET':
        form_student = FormCreateStudent()
        form_user = FromCreateUser()

        context = {
            'form_student':form_student,
            'form_user':form_user
        }
    return render(request, 'crudStudent/create.html',context)