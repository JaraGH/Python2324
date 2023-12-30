from django import forms


class EmployeeForm(forms.Form):
    first_name = forms.CharField(required=True, max_length=20)
    last_name = forms.CharField(required=True, max_length=20)
    email = forms.EmailField()
    date_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    photo = forms.ImageField(required=False)
