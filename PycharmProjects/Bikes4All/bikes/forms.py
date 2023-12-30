from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.forms import TextInput

from bikes.models import UsedBikes


class BikeForm(forms.ModelForm):
    class Meta:
        model = UsedBikes
        exclude = ['id']
        widgets = {
            "bike_name": TextInput(attrs={'class': 'form-control, title="Enter Bike Name", size="50"'}),
            "price": TextInput(attrs={'class': 'form-control, title="Enter Price"'}),
            "city": TextInput(attrs={'class': 'form-control, title, title="Enter City", size="50"'}),
            "kms_driven": TextInput(attrs={'class': 'form-control, title="Enter kms", size="50"'}),
            "owner": TextInput(attrs={'class': 'form-control, title="Enter Owner", size="50"'}),
            "age": TextInput(attrs={'class': 'form-control, title="Enter Age", size="50"'}),
            "power": TextInput(attrs={'class': 'form-control, title="Enter Power", size="50"'}),
            "brand": TextInput(attrs={'class': 'form-control, title="Enter Brand", size="50"'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "bike_form"
        self.helper.form_method = "post"
        self.helper.form_action = ""
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-lg-3"
        self.helper.field_class = "col-lg-8"
        self.helper.form_show_labels = True
        self.helper.add_input(input_object=Submit('submit', 'Submit', css_class='btn-success'))


