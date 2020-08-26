from django import forms
from accounts.models import Student


class FormCreateStudent(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
                
