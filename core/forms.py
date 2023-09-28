from django import forms


class InquiryForm(forms.Form):
    inputName = forms.CharField(
        max_length=100,
        required=False,
        label='Your Name',
        widget=forms.TextInput(
            attrs={'class': 'form-control'})
    )
    inputEmail = forms.EmailField(
        max_length=100,
        label='Your Email*',
        widget=forms.EmailInput(
            attrs={'class': 'form-control'})
    )
    inputSubject = forms.CharField(
        max_length=100,
        required=False,
        label='Your Subject',
        widget=forms.TextInput(
            attrs={'class': 'form-control'})
    )
    inputMessage = forms.CharField(
        label='Your Message*',
        widget=forms.Textarea(
            attrs={'class': 'form-control'})
    )
