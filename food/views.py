from django.shortcuts import render
from django.views import View
from food.models import Category, Product
from django.views.generic import TemplateView, ListView
from .forms import ContactUsForm



class HomeView(TemplateView):
    template_name = 'food/home.html'


class CategoryList(View):

    def get(self, request, id=None):
        products = Product.objects.all()
        if id:
            cat = Category.objects.get(id=id)
            products = Product.objects.filter(category = cat)
            return render(request, 'food/product.html',context={'products':products, 'categories':Category.objects.all()})
        categories = Category.objects.all()
        context = {'products':products, 'categories':categories}
        return render(request, 'food/product.html',context )



class ProductList(ListView):
    model = Product
    queryset = Product.objects.all()
    context_object_name = 'products'
    template_name = 'food/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context['categories'] = categories
        return context

    def get(self, request, id=None):
        products = Product.objects.all()
        if id:
            category = Category.objects.get(id=id)
            products = Product.objects.filter(category=category)
            return render(request, 'food/product.html', context={'products':productss, 'categories':Category.objects.all()})
        categories = Category.objects.all()
        context = {'products':products, 'categories':categories}
        return render(request, 'food/product.html', context)


class About(TemplateView):
    template_name = 'food/about.html'


def customer_detail_form(request):
    if request.method == 'GET':
        form = ContactUsForm()
        return render(request, 'food/checkout.html', context={'form':form})
        
    else:
        print(request.POST)
        form = ContactUsForm(request.POST)
        if form.is_valid():
            return render(request, 'food/thankyou.html')
        else:
            print(form.errors)
            return render(request, 'food/checkout.html', context={'form':form})
