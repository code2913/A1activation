from django.urls import path
from . import views
app_name = "pages"
urlpatterns = [
    path('',views.Homepage.as_view(),name="homepage"),
    path('about-us/',views.AboutUs.as_view(),name="about-us"),
    path('service/',views.Service.as_view(),name="service"),
    path('contact/',views.Contact.as_view(),name="contact"),
]
