from django.shortcuts import render
from myApp.models import Student
# Create your views here.
from django.urls import reverse_lazy

from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

class StudentCreateView(CreateView):
	model=Student
	fields=('Name','Number','Marks','Address')
	#default Template => Student_form.html

class StudentDetailView(DetailView):
	model=Student

class StudentUpdateView(UpdateView):
	model=Student
	fields=('Name','Number','Marks','Address')

class StudentListView(ListView):
	model=Student

class StudentDeleteView(DeleteView):
	model = Student
	success_url = reverse_lazy('list')