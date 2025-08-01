from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field
from .models import NGO, Event

class NGOForm(forms.ModelForm):
    class Meta:
        model = NGO
        fields = ['name', 'registration_number', 'contact_person', 'email', 
                 'phone_number', 'website', 'address', 'city', 'state']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-8 mb-0'),
                Column('registration_number', css_class='form-group col-md-4 mb-0'),
            ),
            Row(
                Column('contact_person', css_class='form-group col-md-6 mb-0'),
                Column('email', css_class='form-group col-md-6 mb-0'),
            ),
            Row(
                Column('phone_number', css_class='form-group col-md-6 mb-0'),
                Column('website', css_class='form-group col-md-6 mb-0'),
            ),
            'address',
            Row(
                Column('city', css_class='form-group col-md-6 mb-0'),
                Column('state', css_class='form-group col-md-6 mb-0'),
            ),
            Submit('submit', 'Save NGO', css_class='btn btn-primary')
        )

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date_time', 'city', 'state', 
                 'location_details', 'ngo', 'poster']
        widgets = {
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'description': forms.Textarea(attrs={'rows': 4}),
            'location_details': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'title',
            'description',
            Row(
                Column('date_time', css_class='form-group col-md-6 mb-0'),
                Column('ngo', css_class='form-group col-md-6 mb-0'),
            ),
            Row(
                Column('city', css_class='form-group col-md-6 mb-0'),
                Column('state', css_class='form-group col-md-6 mb-0'),
            ),
            'location_details',
            'poster',
            Submit('submit', 'Save Event', css_class='btn btn-success')
        )

class EventFilterForm(forms.Form):
    city = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Filter by city...', 'class': 'form-control'}))
    state = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Filter by state...', 'class': 'form-control'}))