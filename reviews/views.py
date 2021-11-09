from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView

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
class ReviewView(View):
    def get(self, request):
        form = ReviewForm()

        return render(request, "reviews/review.html", {
            "form": form
        })

    def post(self, request):
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")
        
        return render(request, "reviews/review.html", {
            "form": form
        })


#if only get and template :
     
class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

class ReviewsListView(TemplateView):
    template_name = "reviews/review_list.html"
    #to use datas in the template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #access to the models
        reviews = Review.objects.all()
        context["reviews"] = reviews
        return context
