from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Review, Promotion, Review, FAQ, Article, Employee
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["name", "rating", "text"]
        widgets = {
            "text": forms.Textarea(attrs={"rows": 5}),
        }


class ReviewListView(ListView):
    model = Review
    template_name = "reviews.html"
    context_object_name = "reviews"
    paginate_by = 10


class AddReviewView(LoginRequiredMixin, View):
    def get(self, request):
        form = ReviewForm()
        return render(request, "reviews/add_review.html", {"form": form})


class SaveReviewView(LoginRequiredMixin, View):
    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect("reviews:reviews.html")
        return render(request, "reviews/add_review.html", {"form": form})


class PromotionsView(View):
    def get(self, request):
        active_promotions = Promotion.objects.filter(is_active=True)
        archived_promotions = Promotion.objects.filter(is_active=False)

        context = {
            "active_promotions": active_promotions,
            "archived_promotions": archived_promotions,
        }

        return render(request, "promotions.html", context)


class QAView(View):
    def get(self, request):
        faqs = FAQ.objects.all()

        context = {
            "faqs": faqs,
        }
        return render(request, "qa.html", context)


class AboutView(View):
    def get(self, request):
        last = article = Article.objects.last()

        context = {
            "last_article": last,
        }

        return render(request, "about.html", context)


class NewsView(View):
    def get(self, request):
        articles = Article.objects.all()

        context = {
            "articles": articles,
        }

        return render(request, "news.html", context)


class ContactsView(View):
    def get(self, request):
        employees = Employee.objects.all()

        context = {
            "employees": employees,
        }
        return render(request, "contacts.html", context)


def privacy_policy_page(request):
    return render(request, "privacy.html")


def save_review(request):
    if request.method == "POST":
        text = request.POST.get("text")
        rating = request.POST.get("rating")
        name = request.POST.get("name")
        user = None
        if request and hasattr(request, "user"):
            user = request.user
        review = Review.objects.create(text=text, rating=rating, user=user, name=name)

        return redirect("information:reviews")

    return redirect("showroom:product_list")
