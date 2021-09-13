from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import  ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView 
from .models import Review
# Create your views here.


class ReviewView(View):
    def get(self,request):
        form = ReviewForm()
        return render(request, 'reviews/review.html',{
        "form": form
    })


    def post(self,request):
        form =  ReviewForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect("/thank-you")




# def review(request):

#     if request.method == 'POST':
#         # entered_username =  request.POST['username']
#         form =  ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
            
            # Formsda modelsni ulagandan kyn kk emas
            # review = Review(username= form.cleaned_data['username'],review_text= form.cleaned_data['review_text'],rating = form.cleaned_data['rating']) 
            # review.save()
            
            # print(form.cleaned_data)
        # if entered_username == "" and len(entered_name) >= 100:
        #     return render(request, 'reviews/review.html',{
        #         "has_error": True,
        #     })
        # print(entered_username)
    #         return HttpResponseRedirect("/thank-you")
    
    # else:
    #     form = ReviewForm()
        
    # return render(request, 'reviews/review.html',{
    #     "form": form
    # })



class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "this works"
        return context


class ReviewsListView(TemplateView):
    template_name = "reviews/review_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.all()
        context["reviews"] = reviews
        return context
    

class ReviewDetail(TemplateView):
    template_name = "reviews/review_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review_id = kwargs["id"]
        selected_review = Review.objects.get(pk=review_id)
        context["review"] = selected_review 
        return context
    


# def thank_you(request):
#     return render(request,"reviews/thank_you.html",{
#         "has_error": False,
#     })


