from django.http import HttpResponse
from django.shortcuts import render 
from homepage.models import homepage
from homepage.models import homepageright
from homepage.models import Brandimg
from homepage.models import featureproduct
from contactus.models import Contactform
from django.shortcuts import render, get_object_or_404, redirect
from shop.models import Category, Product
from wishlist.models import Wishlist 
import os
import requests
from django.shortcuts import render
from django.core.mail import send_mail

from django.http import HttpResponse
import xml.etree.ElementTree as ET
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.core.mail import send_mail

# views.py
from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib import messages
from django.conf import settings





def homepage_view(request):
    homepagedata= homepage.objects.all()
    homepagerightdata = homepageright.objects.all()
    Brandimgdata = Brandimg.objects.all().order_by('id')
    featureproductdata = featureproduct.objects.all()
    categories = Category.objects.all()
    products = Product.objects.all()
    wishlist_count = Wishlist.objects.filter(user=request.user).count() if request.user.is_authenticated else 0
    data={
        'homepagedata':homepagedata,
        'homepagerightdata':homepagerightdata,
        'Brandimgdata':Brandimgdata,
        'featureproductdata':featureproductdata,
        'categories': categories,
        'products': products,
        'wishlist_count': wishlist_count,
    }
    if request.method == 'POST':
        recipient = request.POST.get('recipient')

        if recipient:
            try:
                send_mail(
                    'Thank You for Subscribing',  # Subject
                    'Thank you for subscribing to our newsletter.',  # Body
                    settings.DEFAULT_FROM_EMAIL,  # From email
                    [recipient],  # To email
                    fail_silently=False,
                )
                messages.success(request, "Email sent successfully!")
            except Exception as e:
                messages.error(request, f"Failed to send email: {str(e)}")
        else:
            messages.error(request, "No recipient provided.")
    return render(request,"index.html",data)
def all_products_view(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    Brandimgdata = Brandimg.objects.all().order_by('id')
    wishlist_count = Wishlist.objects.filter(user=request.user).count() if request.user.is_authenticated else 0
    context = {
        'categories': categories,
        'products': products,
        'Brandimgdata':Brandimgdata,
        'wishlist_count': wishlist_count,
        
    }
    return render(request, 'product-list.html', context)
# Add Product to Wishlist
@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Wishlist.objects.get_or_create(user=request.user, product=product)  # Avoid duplicates
    return redirect('wishlist_view')  # Redirect to wishlist page

# Remove Product from Wishlist
@login_required
def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Wishlist.objects.filter(user=request.user, product=product).delete()
    return redirect('wishlist_view')  # Redirect to wishlist page

def countriesData(request):
    # API URL
    api_url = "https://api.first.org/data/v1/countries"

    # Fetch the data from the API
    response = requests.get(api_url)
    if response.status_code == 200:
        countries_data = response.json()  # Parse the JSON response
        countries = countries_data.get('data', {})  # Extract the 'data' key
    else:
        countries = {}  # Handle the case where the API is not reachable

    # Pass the data to the template
    return render(request, 'print_json.html', {'countries': countries})

# View Wishlist
@login_required
def wishlist_view(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    context = {
        'wishlist_items': wishlist_items,
    }
    return render(request, 'wishlist.html', context)

def category_products_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = category.products.all()
    categories = Category.objects.all()
    Brandimgdata = Brandimg.objects.all().order_by('id')   # Access related products
    data = {
        'category': category,
        'products': products,
        'categories': categories,
        'Brandimgdata':Brandimgdata,
    }
    return render(request, 'product-list.html', data)


def contactus(request):
    msg=""
    if request.method =='POST':
        fullname = request.POST.get('fullname', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()
        if not fullname or not email or not subject or not message:
            msg = "All fields are required. Please fill them out."
        else:
            # Save data to the database
            alldata = Contactform(fullname=fullname, email=email, subject=subject, message=message)
            alldata.save()
            msg = "Your message has been successfully sent."
    return render(request,"contact.html",{'msg':msg})

def read_xml(request):
    # Path to the XML file
    # Path to the XML file
    xml_path = os.path.join("static", "xml", "countries.xml")
    
    # Parse the XML file
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # Extract data (Assuming a structure like <Country><Name>...</Name></Country>)
    countries = []
    for country in root.findall("Country"):  # Adjust 'Country' based on your XML structure
            name = country.find("Name").text if country.find("Name") is not None else "Unknown"
            code = country.find("Code").text if country.find("Code") is not None else "N/A"
            countries.append({"name": name, "code": code})
    # Pass the data to the template
    return render(request, 'print_xml.html', {'countries': countries})



