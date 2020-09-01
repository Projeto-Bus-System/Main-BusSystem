from django.shortcuts import render, redirect
from accounts.forms import FormCreateStudent, FromCreateUser
from django.http import HttpResponse

def createStudent(request):
    if request.method == 'POST':

        form_student = FormCreateStudent(request.POST)
        form_user = FromCreateUser(request.POST)

        if form_student.is_valid() and form_user.is_valid():
            save_user = form_user.save()
            save_student = form_student.save(commit=False)
            save_student.user_id = save_user
            save_student.save()
            return redirect('/')
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