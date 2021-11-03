from django import forms
from django.forms import fields

from reviews.models import Review 

#class ReviewForm(forms.Form):
#    user_name = forms.CharField(label="Your name", max_length=50, error_messages={
#        "required": "Your name must not be empty",
#        "max_lenght": "Please enter a shorter name"
#    })
#    review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=200)
#    rating = forms.IntegerField(label="Your rating", min_value=0, max_value=20)

#instead of that, we can use directely the models

class ReviewForm(forms.ModelForm):
    #we indicate wich model is related
    class Meta:
        model = Review
        #wich fields are included. If all : '__all__'
        #all but one excluded would be : exclude = ['owner_comment'] for instance
        fields= '__all__'
        #to change the name on the inputs forms (what will see the user)
        labels = {
            'user_name': 'Your Name',
            'review_text':'Your Feedback',
            'rating':'Your rating'
        }
        error_messages = {
            'user_name':{
                "required": "Your name must not be empty",
                "max_lenght": "Please enter a shorter name"
            }
    
        }