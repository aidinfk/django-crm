from django.contrib import admin
from django.urls import path, include
from dashboard.views import dashboard_webpage, about_us_page
from contacts.views import contacts_list_view, contacts_detail_view


urlpatterns = [
    path("", dashboard_webpage),
    path("contacts/<int:contact_id>/", contacts_detail_view),
    path("contacts/", contacts_list_view),
    path("dashboard/", dashboard_webpage),
    path("about/", about_us_page),
    path("admin/", admin.site.urls),
    path("auth/", include("django_googler.urls.default")),
]
