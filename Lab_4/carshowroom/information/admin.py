from django.contrib import admin
from .models import Article, FAQ, Employee, Review, Promotion


class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "summary", "image", "content"]
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Article, ArticleAdmin)


class FAQAdmin(admin.ModelAdmin):
    list_display = ["question", "answer", "date_added"]


admin.site.register(FAQ, FAQAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["name", "photo", "description", "phone", "email"]
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Employee, EmployeeAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ["user", "name", "rating", "text", "date_added"]
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Review, ReviewAdmin)


class PromotionAdmin(admin.ModelAdmin):
    list_display = ["code", "description", "is_active"]
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Promotion, PromotionAdmin)
