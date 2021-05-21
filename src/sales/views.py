from django.shortcuts import render
from django.views.generic import ListView
from .models import Sale

# Create a home view and a template for it



def home_view(request):
  hello = 'hello world from the view'
  return render(request, 'sales/home.html', {'h': hello})

class SalesListView(ListView):
  model = Sale
  template_name = 'sales/main.html'







# Create your views here.


