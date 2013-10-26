from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    subject.widget.attrs.update({'class' : 'form-control', 'placeholder':'Subject'})
    message = forms.CharField(widget=forms.Textarea)
    message.widget.attrs.update({'class' : 'form-control', 'placeholder':'Anything you would like to tell us...'})
    sender = forms.EmailField()
    sender.widget.attrs.update({'class' : 'form-control', 'placeholder':'Your Email'})
