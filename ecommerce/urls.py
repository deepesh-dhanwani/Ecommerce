"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from ecommerce import views

from django.conf import settings
from django.conf.urls.static import static
from . import views  # Importing views from the same app

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.homepage_view, name="home"),
    path("contact/", views.contactus, name="contact"),
    path("products/", views.all_products_view, name="all_products"),
    path("category/<int:category_id>/", views.category_products_view, name="category_products"),
    path("wishlist/", views.wishlist_view, name="wishlist_view"),
    path("wishlist/add/<int:product_id>/", views.add_to_wishlist, name="add_to_wishlist"),
    path("wishlist/remove/<int:product_id>/", views.remove_from_wishlist, name="remove_from_wishlist"),
    path("countries-json-format/", views.countriesData, name="country"),
    path("countries-xml-format/", views.read_xml, name="conxml"),
    # path("send-email/", views.send_email, name="send_email"),  # Added email-sending URL
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)