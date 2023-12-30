from django import forms

from sports.models import Sport

SPORT_TYPES = {
        "M": "Motor",
        "B": "Ball Sport",
        "W": "Water Sport",
        "A": "Air Sport",
        "K": "Bikes",
        "T": "Athletics",
        "F": "Fighting",
    }


class SportForm(forms.ModelForm):
    class Meta:
        model = Sport
        fields = '__all__'



## forms.Form
# class SportForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     description = forms.CharField(max_length=200)
#     is_outdoor = forms.BooleanField(initial=False, widget=forms.CheckboxInput(),
#                                     required=False)
#     number_players = forms.IntegerField(initial=2, min_value=1, max_value=100)
#     type = forms.CharField(max_length=1,
#                            widget=forms.Select(choices=SPORT_TYPES.items()))
#     origin = forms.CharField(max_length=50, initial='Unknown')
#     image = forms.ImageField(required=False)


