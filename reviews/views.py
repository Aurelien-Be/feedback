from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView

from .forms import ReviewForm
#to access to datas for the view list class:
from .models import Review

# Create your views here.

      

#def review(request):
#    if request.method == 'POST':
#        form = ReviewForm(request.POST)

#        if form.is_valid():
#          form.save()
#          return HttpResponseRedirect("/thank-you")
#    else:
#      form = ReviewForm()

#      return render(request, "reviews/review.html", {
#        "form": form
#    })

#instead, we can use a  class based view in order to avoid 'if request.method = POST'
#class ReviewView(View):
#    def get(self, request):
#        form = ReviewForm()

#        return render(request, "reviews/review.html", {
#            "form": form
#        })

#    def post(self, request):
#        form = ReviewForm(request.POST)

#        if form.is_valid():
#            form.save()
#            return HttpResponseRedirect("/thank-you")
        
#        return render(request, "reviews/review.html", {
#            "form": form
#        })

#or even more specific, the FormView:

class ReviewView(FormView):
    form_class = ReviewForm
    template_name = "reviews/review.html"  #thieses 2 lines replace the get method
    #for the post:
    success_url = "/thank-you"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

#if only get and template, use TemplateView :
     
class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    #with ListVView, jango will fetch all the data related to that module and pass it as context to this template
    #in the template, we have to search datas from object_list 
    #we can overwhrite it with context_object_name = 

    #to render only some datas:
    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gt=12)
        return data 

#class DetailedReview(TemplateView):
#    template_name = "reviews/detailed_review.html"

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
        #key id to connect to urls
#        review_id = kwargs["id"]
        #access to the models
#        detailed_review = Review.objects.get(pk=review_id)
        #add a key
 #       context["review"] = detailed_review
#        return context
#Instead of that, it is possible to use the detailed view


class DetailedReview(DetailView):
    template_name = "reviews/detailed_review.html"
    model = Review