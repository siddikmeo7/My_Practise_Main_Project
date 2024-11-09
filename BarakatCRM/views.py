from django.views import generic
from django.urls import reverse_lazy
from .models import *

# Products
class ProductsView(generic.ListView):
    model = Product
    template_name = "base.html"
    fields = "__all__"
    def get_queryset(self):
        return Product.objects.all().order_by('index')

class DetailProduct(generic.DetailView):
    model = Product
    template_name = "product_detail.html"

class AddProduct(generic.CreateView):
    model = Product
    fields = "__all__"
    template_name = 'product_form.html'
    success_url = reverse_lazy('Base-Page')


class EditProduct(generic.UpdateView):
    model = Product
    fields = "__all__"
    template_name = 'product_form.html'
    success_url = reverse_lazy('Base-Page')

class DeleteProduct(generic.DeleteView):
    model = Product
    fields = "__all__"
    template_name = 'confdelproduct.html'
    success_url = reverse_lazy('Base-Page')

# Clients 

class ClientsListView(generic.ListView):
    model = Client
    fields = "__all__"
    template_name = 'clients_list.html'

class AddClient(generic.CreateView):
    model = Client
    fields = "__all__"
    template_name = 'clients_form.html'
    success_url = reverse_lazy('Clients-List')

class DetailClient(generic.DetailView):
    model = Client
    template_name = "client_detail.html"


class EditClient(generic.UpdateView):
    model = Client
    fields = "__all__"
    template_name = 'clients_form.html'
    success_url = reverse_lazy('Clients-List')

class DeleteClient(generic.DeleteView):
    model = Client
    fields = "__all__"
    template_name = 'confdelclient.html'
    success_url = reverse_lazy('Clients-List')