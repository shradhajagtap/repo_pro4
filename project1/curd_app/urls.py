from django.urls import path
from .views import company_view, show_company, update_view, cancel_view

urlpatterns = [
    path("", company_view, name="company_url"),
    path("show/", show_company, name="show_url"),
    path("update/<int:pk>", update_view, name="update_url"),
    path("cancel/<int:pk>", cancel_view, name="cancel_url")
]
