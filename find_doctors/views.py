from django.shortcuts import render
from django.contrib import messages


from django.shortcuts import render, redirect, get_object_or_404

from .forms import PatientForm
from .models import Patients, Doctor


# Create your views here.

def create_view(request):
  form = PatientForm()
  if request.method == 'POST':
    form = PatientForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, 'Create successfully.')
      return redirect('/')
  return render(request, 'find_doctors/home.html', {'form': form})


# AJAX
def load_doctors(request):
  department_id = request.GET.get('department_id')
  doctors = Doctor.objects.filter(department_id=department_id).all()
  return render(request, 'find_doctors/doctor_dropdown_list_options.html', {'doctors': doctors})