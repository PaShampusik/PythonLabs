from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Review
from .models import Promotion
from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'rating', 'text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 5}),
        }

class ReviewListView(ListView):
    model = Review
    template_name = 'reviews/review_list.html'
    context_object_name = 'reviews'
    paginate_by = 10

class AddReviewView(LoginRequiredMixin, View):
    def get(self, request):
        form = ReviewForm()
        return render(request, 'reviews/add_review.html', {'form': form})

class SaveReviewView(LoginRequiredMixin, View):
    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('reviews:review_list')
        return render(request, 'reviews/add_review.html', {'form': form})
    
class PromotionsView(View):
    def get(self, request):
        active_promotions = Promotion.objects.filter(is_active=True)
        archived_promotions = Promotion.objects.filter(is_active=False)

        context = {
            'active_promotions': active_promotions,
            'archived_promotions': archived_promotions
        }

        return render(request, 'promotions.html', context)
def about_page(request):
    return render(request, "about.html")


def news_page(request):
    return render(request, "news.html")


def contacts_page(request):
    return render(request, "contacts.html")


def qa_page(request):
    return render(request, "qa.html")


def privacy_policy_page(request):
    return render(request, "privacy.html")


def reviews_page(request):
    return render(request, "reviews.html")


def promotions_page(request):
    return render(request, "promotions.html")
