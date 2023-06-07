from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Feedback
from django.contrib import messages
from django.views import View

from .forms import FeedbackForm

class IndexView(View):
    def get(self, request):
        user = "nirendrarawal"
        product_numb = 7
        products = Product.objects.all().order_by('id')[:4]#Limit the number of objects to show on template
        return render(request, "products/home.html", {
            "name": user,
            "product_numb": product_numb,
            "products": products
    })
    def post(self, request):
        pass

def index(request):
    user = "nirendrarawal"
    product_numb = 7
    products = Product.objects.all().order_by('id')[:4]#Limit the number of objects to show on template
    return render(request, "products/home.html", {
        "name": user,
        "product_numb": product_numb,
        "products": products
    })
    
    
def signup(request):
    return render(request, "products/signup.html")
  
def product_cat(request, product):
    if product == "suits" or product == "dresses" or product == "shirts" or product == "shoes":
        return HttpResponse(f"Here is the list of our {product}.")
    else:
        return HttpResponse("The page you are looking for doesn't exist!")


class ProductPageView(View):
    def get(self, request, product_brand, product_slug):
        product = Product.objects.get(slug = product_slug)
        my_feedback = Feedback.objects.get(product = product, id=1)
        form = FeedbackForm(instance=my_feedback)
        reviews = Feedback.objects.filter(product = product)
        return render(request, "products/product.html", {
            "product": product,
            "form": form,
            "reviews":reviews
    })
        
    def post(self, request, product_brand, product_slug):
        product = Product.objects.get(slug = product_slug)
        my_feedback = Feedback.objects.get(product = product, id=1)
        form = FeedbackForm(request.POST, instance=my_feedback)
        reviews = Feedback.objects.filter(product = product)
        if form.is_valid():
            form.save()
            messages.success(request, "Your feedback was submitted successfully!")
            
        
        return render(request, "products/product.html", {
            "product": product,
            "form": form,
            "reviews":reviews
        
    })

def product_page(request, product_brand, product_slug):
    product = Product.objects.get(slug = product_slug)
    my_feedback = Feedback.objects.get(product = product, id=1)
    form = FeedbackForm(instance=my_feedback)
    reviews = Feedback.objects.filter(product = product)
    if request.method == "GET":
        return render(request, "products/product.html", {
        "product": product,
        "form": form,
        "reviews":reviews
    })
    else:
        form = FeedbackForm(request.POST, instance=my_feedback)
        if form.is_valid():
            # feedback = Feedback(
            #     name = form.cleaned_data["name"],
            #     rating = form.cleaned_data["rating"],
            #     product = product,
            #     text = form.cleaned_data["text"]
            # )
            # feedback.save()
            form.save()
            messages.success(request, "Your feedback was submitted successfully!")
            
        
        return render(request, "products/product.html", {
        "product": product,
        "form": form,
        "reviews":reviews
        
    })
    