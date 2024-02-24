from django import forms
from captcha.fields import CaptchaField
from website.models import Contact,NewsLetter



class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model=Contact
        fields='__all__'


class NewsLetterForm(forms.ModelForm):
    class Meta:
        model=NewsLetter
        fields='__all__'