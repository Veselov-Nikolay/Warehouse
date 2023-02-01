from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import Room, Shelf, Client, Product


def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'inventory/room_list.html', {'rooms': rooms})

def room_detail(request, pk):
    room = get_object_or_404(Room, pk=pk)
    return render(request, 'inventory/room_detail.html', {'room': room})

def shelf_list(request):
    shelves = Shelf.objects.all()
    return render(request, 'inventory/shelf_list.html', {'shelves': shelves})

def shelf_detail(request, pk):
    shelf = get_object_or_404(Shelf, pk=pk)
    return render(request, 'inventory/shelf_detail.html', {'shelf': shelf})

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'inventory/client_list.html', {'clients': clients})

def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    products = Product.objects.filter(client=client)
    return render(request, 'inventory/client_detail.html', {'client': client, 'products': products})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'inventory/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'inventory/product_detail.html', {'product': product})

# from django.shortcuts import render
# from .models import Room, Shelf, Client, Product

def storage_view(request):
    rooms = Room.objects.all()
    shelves = Shelf.objects.all()
    clients = Client.objects.all()
    products = Product.objects.all()
    context = {
        'rooms': rooms,
        'shelves': shelves,
        'clients': clients,
        'products': products,
    }
    return render(request, 'storage.html', context)


def index(request):
    rooms = Room.objects.all()
    shelves = Shelf.objects.all()
    clients = Client.objects.all()
    products = Product.objects.all()
    return render(request, 'index.html', {'rooms': rooms, 'shelves': shelves, 'clients': clients, 'products': products})
