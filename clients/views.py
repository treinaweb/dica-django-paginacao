from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView

from .models import Client


def list_clients(request):
    clients = Client.objects.all()
    paginator = Paginator(clients, 2)

    page = request.GET.get("page", 1)
    page_obj = paginator.get_page(page)

    return render(request, 'clients/client_list.html', {'client_list': page_obj})


class ClientList(ListView):
    model = Client
    paginate_by = 2
    page_kwarg = 'pagina'