from django import forms
from onlineapp.models import College,Student,MockTest1

class addStudent(forms.ModelForm):
    class Meta:
        model=Student
        exclude=['id','dob','college']
        widgets={

            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'enter'}),

            'db_folder': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter'}),

            'dropped_out': forms.CheckboxInput(attrs={'class': 'form-control', 'placeholder': 'enter'}),

        }


class addCollege(forms.ModelForm):
    class Meta:
        model=College
        exclude=['id']
        widgets={

            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'enter'}),

            'location': forms.TextInput(attrs={'class':'form-control','placeholder':'enter'}),

            'acronym':forms.TextInput(attrs={'class':'form-control','placeholder':'enter'}),

            'contact': forms.EmailInput(attrs={'class':'form-control','placeholder':'enter'}),
        }


class addMockTest(forms.ModelForm):
    class Meta:
        model=MockTest1
        exclude=['id','total','student']
        widgets = {

            'problem1': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Score in problem 1'}),

            'problem2': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Score in problem 2'}),

            'problem3': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Score in problem 3'}),

            'problem4': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Score in problem 4'}),

        }