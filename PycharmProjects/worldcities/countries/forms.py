from django import forms

from countries.models import Country


# class CountryForm(forms.Form):
#     name = forms.CharField(label='name', max_length=50)
#     continent = forms.CharField(label='continent', max_length=50)

class CountryForm(forms.ModelForm):
    #id = forms.IntegerField()
    name = forms.CharField(required=True)
    continent = forms.CharField(required=True, max_length=50, min_length=1)

    class Meta:
        model = Country
        fields = ['name', 'continent']
