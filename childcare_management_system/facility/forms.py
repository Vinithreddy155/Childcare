from django import forms

class FacilityForm(forms.Form):
    name = forms.CharField(label='Name of Facility', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label='Address', max_length=300, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
    phone_number = forms.CharField(label='Phone Number', max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    admin_name = forms.CharField(label='Admin Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    admin_email = forms.EmailField(label='Admin Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    admin_contact = forms.CharField(label='Admin Contact', max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    license_number = forms.CharField(label='License Number', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
