from django.shortcuts import render
from django.http import HttpResponseRedirect, request
from .forms import  ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView 
from django.views.generic import ListView, DetailView
# from django.views.generic.edit import FormView  buni o'rniga CreateViewni ishlatamiz 
from django.views.generic.edit import CreateView
from .models import Review
# Create your views here.


class ReviewView(CreateView):
    model = Review
    # fields = "__all__"
    form_class = ReviewForm
    # form_class = ReviewForm
    template_name = 'reviews/review.html'
    success_url = "/thank-you"

    
      
    # def get(self,request):
    #     form = ReviewForm()
    #     return render(request, 'reviews/review.html',{
    #     "form": form
    # })


    # def post(self,request):
    #     form =  ReviewForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #     return HttpResponseRedirect("/thank-you")




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


class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    # context_object name bu htmlda ishlatish ucun yozildi yozilmasa ham buladi unda objet_list yoziw kk
    context_object_name = "reviews"

# filter qilish bu Lisstviewda misol
    # def get_queryset(self):
    #     base_query= super().get_queryset()
    #     data = base_query.filter(rating__gt=5)
    #     return data
    


# TemplateView =ni udalit qilindi endi Listview bilan ishlaymiz wuning ucun kk emas 
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     reviews = Review.objects.all()
    #     context["reviews"] = reviews
    #     return context
    

class ReviewDetail(DetailView):
    template_name = "reviews/review_detail.html"
    model = Review

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session.get("favorite_review")
        context["is_favorite"] = favorite_id == str(loaded_review.id)
        return context





    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     review_id = kwargs["id"]
    #     selected_review = Review.objects.get(pk=review_id)
    #     context["review"] = selected_review 
    #     return context
    


# def thank_you(request):
#     return render(request,"reviews/thank_you.html",{
#         "has_error": False,
#     })


class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST['review_id']
        # fav_review = Review.objects.get(pk=review_id)
        request.session['favorite_review'] = review_id
        return HttpResponseRedirect("/reviews/"+ review_id)