from django import forms
from .models import Contact, Category

class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget = forms.FileInput(
            attrs={"accept":"image/*"}
        )
        
    )
    class Meta:
        model = Contact        
        fields = ["first_name","last_name","phone",
                  "email", "description", "category","picture",
                  ]