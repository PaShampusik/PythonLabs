from django.urls import path
from . import views

app_name = "information"

urlpatterns = [
    path("about/", views.about_page, name="about"),
    path("privacy/", views.privacy_policy_page, name="privacy_policy"),
    path("news/", views.news_page, name="news"),
    path("contacts/", views.contacts_page, name="contacts"),
    path("qa/", views.qa_page, name="qa"),
    path("privacy-policy/", views.privacy_policy_page, name="privacy_policy"),
    path("reviews/", views.reviews_page, name="reviews"),
    path("promotions/", views.promotions_page, name="promotions"),
    path('add/', views.AddReviewView.as_view(), name='add_review'),
    path('save/', views.SaveReviewView.as_view(), name='save_review'),
]
