from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        # fields = "__all__"
        # exclude = ['product']
        fields = ['name', 'rating', 'text']
        labels = {'name': 'Full Name', 'text': 'Your Feedback'}

"""
class FeedbackForm(forms.Form):
    name = forms.CharField(required=True, error_messages={"required":"Your forgot to add your name!"})
    rating = forms.IntegerField( min_value=1, max_value=5)
    text = forms.CharField(widget=forms.Textarea)
    
    
    # HOW TO ADD AN ID AND CLASS IN DJANGO FORMS
    # name = forms.CharField(widget=forms.TextInput(attrs={'class':'class2', 'id':'id2'}),required=True, error_messages={"required":"Your forgot to add your name!"})
    # rating = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'class3', 'id':'id3'}, min_value=1, max_value=5))
    # text = forms.CharField(label="Your Feedback", widget=forms.Textarea(attrs={'class':'class1', 'id':'id1'}), max_length=200)
    
    """