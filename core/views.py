from django.shortcuts import render, redirect
from django.views import View
from .models import Student
from .forms import AddStudentForm
# Create your views here.

class Home(View):
    def get(self, request):
        stud_data = Student.objects.all()
        return render(request, './core/home.html', {'studdata':stud_data})
    
class Add_Stud(View):
    def get(self, request):
        fm = AddStudentForm()
        return render(request, './core/add_stud.html', {'form':fm})
    
    def post(self, request):
        fm = AddStudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return render(request, './core/add_stud.html', {'form':fm})
        
class Delete_Student(View):
    def post(self, request):
        data = request.POST
        id = data.get('id')
        studdata = Student.objects.get(id=id)
        studdata.delete()
        return redirect('/')

class Update_Stud(View):
    def get(self, request, id):
        stud = Student.objects.get(id=id)
        fm = AddStudentForm(instance=stud)
        return render(request, 'core/update_stud.html', {'form':fm})
            
    def post(self, request, id):
        stud = Student.objects.get(id=id)
        fm = AddStudentForm(request.POST, instance=stud)
        if fm.is_valid():
            fm.save()
            return redirect('/')            


