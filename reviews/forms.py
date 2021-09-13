from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#     username = forms.CharField(label="Azamat",max_length=100, error_messages={
#         "required":"Your name must not be empty",
#         "max_lenght": "please enter the name"
#     })
#     review_text = forms.CharField(label="Your feedback", widget=forms.Textarea, max_length=200)
#     rating  = forms.IntegerField(label="Your Rating", min_value=1,max_value=5)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # Hammasinin uz ichiga oladi
        fields = "__all__" 
        # exclude = ['username'] faqat wuni uz ichiga olmaydi modelsdan
        labels = {
            "username": "Your Name",
            "review_text": "Your Text",
            "rating": "Rating"
        }
        error_messages = {
            "username": {
                "requried": "Your name must not be empty",
                "max_lenght": "please enter the name",

            }
        }
