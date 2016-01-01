from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    message = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
    
    # def __init__(self, *args, **kwargs):
    #     super(ContactForm, self).__init__(*args, **kwargs)
    #     self.fields['subject'].label = "Subject..:"
    #     self.fields['contact_email'].label = "Your email:"
    #     self.fields['message'].label ="What do you want to say?"
