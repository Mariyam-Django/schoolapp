from django import forms
from onlineschool.models import *

class StudentForm(forms.ModelForm):
    # class Meta:
    #     model=Student
    #     fields="__aLL__"
    #
    #     widgets={'name':forms.TextInput(attrs={'class':'form-control'}),
    #           'email': forms.TextInput(attrs={'class': 'form-control'}),
    #          }
    class Meta:
        model=Student
        fields='__all__'
        widgets={'name':forms.TextInput(attrs={'placeholder':'Name','style':'color:orange'}),
                 'email':forms.EmailInput(attrs={'placeholder':'Email'}),
                 'address':forms.Textarea(attrs={'rows':8, 'cols':25,'placeholder':'Address'}),
                 'phone':forms.NumberInput(attrs={'placeholder':'Phone','style':'color:red'}),


                 }
    # def clean(self):
    #     cleaned_data=self.cleaned_data
    #     name=cleaned_data.get("name")
    #     phone=cleaned_data.get("phone")
    #
    #     if len(name)<=6:
    #         self.add_error("name","Name minimum 6 chars")
    #     if  len(phone)!=10:
    #         self.add_error("phone","Phone number only 10 difits ")
    #     else:
    #         return  cleaned_data
    def clean(self):
        cleaned_data=self.cleaned_data
        name=cleaned_data.get('name')
        phone=cleaned_data.get('phone')

        if len(name)<=6:
            self.add_error('name','name minimum 6 chars')
        if len(phone)!=10:
            self.add_error('phone','phone num only 10 dig')
        else:
            return cleaned_data


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())

class IdForm(forms.ModelForm):
    class Meta:
        model=Identity
        fields='__all__'
class IdModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name

class StudentChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name
class PersonForm(forms.ModelForm):
    class Meta:
        model=Person
        fields='__all__'

    identity = IdModelChoiceField(queryset=Identity.objects.all(),
                                  widget=forms.Select(attrs={'class': 'form-control', 'blank': 'Select Vehicle'}))

class EnrollForm(forms.ModelForm):
    class Meta:
        model=Enroll
        fields='__all__'
    student=StudentChoiceField(queryset=Student.objects.all(),
                                  widget=forms.Select(attrs={'class': 'form-control', 'blank': 'Select '}))

