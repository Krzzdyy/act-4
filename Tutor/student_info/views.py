from django.shortcuts import render, redirect,get_object_or_404
from .models import Student
def index(request):
    if request.method == 'POST':
             
        student_id = request.POST.get("student_id")
        name = request.POST.get("name")
        year_section = request.POST.get("year_section")

        newstudent = Student(
              student_id = student_id,
              name = name,
              year_section = year_section
           )
        newstudent.save()
        return redirect('index') 
    return render(request, 'student_info/index.html')

#view studentss
def read(request):
    students = Student.objects.all()
    return render(request, 'student_info/read.html', {'students': students})

# UPDATE 
def update(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.student_id = request.POST.get("student_id")
        student.name = request.POST.get("name")
        student.year_section = request.POST.get("year_section")
        student.save()
        return redirect('read')

    return render(request, 'student_info/update.html', {'student': student})

#delte
def delete(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('read')