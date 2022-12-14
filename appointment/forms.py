from django import forms
from .models import Patients, Doctor


class PatientForm(forms.ModelForm):
  class Meta:
    model = Patients
    # fields = '__all__'
    exclude = ['user', ]

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['doctor'].queryset = Doctor.objects.none()

    if 'department' in self.data:
      try:
        department_id = int(self.data.get('department'))
        self.fields['doctor'].queryset = Doctor.objects.filter(department_id=department_id).order_by('name')
      except (ValueError, TypeError):
        pass  # invalid input from the client; ignore and fallback to empty City queryset
    elif self.instance.pk:
      self.fields['doctor'].queryset = self.instance.department.doctor_set.order_by('name')
  
  def read_user(self):
    if self.instance: 
        return self.instance.sku
    else: 
        return self.fields['sku']

  
class PatientAppointmentAnswerForm(forms.Form):
  test =forms.CharField()
  medicine_one =forms.CharField()
  medicine_two =forms.CharField()
  medicine_three =forms.CharField()
  medicine_others =forms.CharField()
  advice =forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20, 'placeholder': 'Thana, Road number, Home number, Area, Others info..'}))

  def __str__(self):
    return f"{self.medicine_one}"