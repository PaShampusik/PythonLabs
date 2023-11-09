from django.urls import path
from . import views

app_name = "information"

urlpatterns = [
    path("about/", views.AboutView.as_view(), name="about"),
    path("privacy/", views.privacy_policy_page, name="privacy_policy"),
    path("news/", views.NewsView.as_view(), name="news"),
    path("contacts/", views.ContactsView.as_view(), name="contacts"),
    path("qa/", views.QAView.as_view(), name="qa"),
    path("reviews/", views.ReviewListView.as_view(), name="reviews"),
    path("table/", views.TableView.as_view(), name="table"),
    path("promotions/", views.PromotionsView.as_view(), name="promotions"),
    path('check_promo/<str:promo>', views.CheckPromotionsView.as_view(), name='check_promo'),
    path("add/", views.AddReviewView.as_view(), name="add_review"),
    path("save/", views.SaveReviewView.as_view(), name="save_review"),
    path("save_review", views.save_review, name="save_review"),
]
