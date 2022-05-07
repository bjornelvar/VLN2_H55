from django.shortcuts import render
from items.models import Items

# Create your views here.

def index(response):
    return render(response, 'home/home-index.html')


def search_items(request):
    if request.method == 'POST':
        search_term = request.POST['search_term']
        return render(request, 'items/search_items.html', {'search_term': search_term, 'items': Items.objects.filter(name__icontains=search_term)})
    else:
        return render(request, 'items/search_items.html', {})