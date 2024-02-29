
from django import forms
from .models import *

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'append_dateline']

    def __init__(self, *args, **kwargs):
        super(JobForm, self).__init__(*args, **kwargs)
        # Add any additional customization for form fields if needed




class PersonForm(forms.ModelForm):
    class Meta:
        model = Personal_Infor
        fields = ['Surname','First_name','last_name','email','Gender','marital_status','phone_number']

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        # Add any additional customization for form fields if needed

    def clean(self):
        cleaned_data = super().clean()
        # Add any additional validation or cleaning logic if needed

class UpdateForm(forms.ModelForm):
    class Meta:
        model = updateform
        fields = ['title', 'Education','cover_letter','cv']
        # Exclude the person field from the form as it should be set automatically
        exclude = ['person']

    def __init__(self, *args, **kwargs):
        super(UpdateForm, self).__init__(*args, **kwargs)
        # Add any additional customization for form fields if needed

    def clean(self):
        cleaned_data = super().clean()
        # Add any additional validation or cleaning logic if needed


class RefereeForm(forms.ModelForm):
    class Meta:
        model = Referee
        fields = '__all__'
        exclude = ['person']

    def __init__(self, *args, **kwargs):
        super(RefereeForm, self).__init__(*args, **kwargs)
class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name']
        

    def __init__(self, *args, **kwargs):
        super(DepartmentForm, self).__init__(*args, **kwargs)
class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = '__all__'
        

    def __init__(self, *args, **kwargs):
        super(ProgramForm, self).__init__(*args, **kwargs)
class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['name', 'code', 'credits', 'department', 'program','semester']
        exclude = ['lecture','student']

    def __init__(self, *args, **kwargs):
        super(UnitForm, self).__init__(*args, **kwargs)
class UnitSelectionForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['name']  # Assuming 'name' is the field representing the unit name
        widgets = {
            'name': forms.CheckboxSelectMultiple,  # Using checkboxes for unit selection
        }
class YearForm(forms.ModelForm):
    class Meta:
        model = AcademicYear
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(YearForm, self).__init__(*args, **kwargs)
class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SemesterForm, self).__init__(*args, **kwargs)