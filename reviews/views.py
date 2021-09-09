from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import  ReviewForm
from .models import Review
# Create your views here.
def review(request):

    if request.method == 'POST':
        # entered_username =  request.POST['username']
        form =  ReviewForm(request.POST)
        if form.is_valid():
            review = Review(username= form.cleaned_data['username'],review_text= form.cleaned_data['review_text'],rating = form.cleaned_data['rating']) 
            review.save()
            
            # print(form.cleaned_data)
        # if entered_username == "" and len(entered_name) >= 100:
        #     return render(request, 'reviews/review.html',{
        #         "has_error": True,
        #     })
        # print(entered_username)
            return HttpResponseRedirect("/thank-you")
    
    else:
        form = ReviewForm()
        
    return render(request, 'reviews/review.html',{
        "form": form
    })



def thank_you(request):
    return render(request,"reviews/thank_you.html",{
        "has_error": False,
    })