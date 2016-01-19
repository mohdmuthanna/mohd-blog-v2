from django import forms

from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget



class ContactForm(forms.Form):
    subject = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Subject', 'class':'form-control',}),
    )

    contact_email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email', 'class':'form-control',}),
    )

    message = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'placeholder': 'Enter your message', 'class':'form-control',}),
    )

    captcha = ReCaptchaField(label="", required=True, widget=ReCaptchaWidget())

    # def __init__(self, *args, **kwargs):
    #     super(ContactForm, self).__init__(*args, **kwargs)
    #     self.fields['subject'].placeholder = "Subject..:::::"
    #     self.fields['contact_email'].label = "Your email:::::"

    #     self.fields['message'].label ="What do you want to say?"

    #  class Meta:
    #     model = YourModelName
    #     widgets = {
    #         'username' : forms.TextInput(attrs = {'placeholder': 'Username'}),
    #         'email'    : forms.TextInput(attrs = {'placeholder': 'E-Mail'}),
    #     }
