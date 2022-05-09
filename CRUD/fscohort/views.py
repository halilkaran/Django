 
from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student
from django.contrib import messages


def index(request):
    return render(request, 'fscohort/index.html')



def student_list(request):
    students  = Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, 'fscohort/student_list.html', context)



def student_add(request):
    form = StudentForm() # boş form render edeceğiz
    if request.method == 'POST':          
        print(request.POST)				   
        form = StudentForm(request.POST)   
        if form.is_valid():				   
            form.save()
            messages.success(request, "student created succesfully!")
            return redirect("list")					   
    context = {
        'form' : form
    }
    return render(request, 'fscohort/student_add.html', context)


def student_update(request, id):
    student =Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method== "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            
            form.save()
            messages.success(request, "student updated succesfully!")
            return redirect("list")
            
    context = {
        'form':form,
    }
    return render(request, 'fscohort/student_update.html', context)

def student_delete(request, id):
    # student = get_object_or_404(Student, id=id)
    student = Student.objects.get(id=id)
    if request.method == "POST":
        student.delete()
        messages.error(request, "student deleted succesfully!")
        return redirect("list")
    return render(request, "fscohort/student_delete.html") 

def student_detail(request, id):        
    student = Student.objects.get(id=id)
    context = {
        'student': student
    }
    return render(request, 'fscohort/student_detail.html', context)



