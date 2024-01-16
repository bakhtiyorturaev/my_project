from django.shortcuts import render
from .models import Noutbuk
# Create your views here.


def noutbuks_list(request):
    noutbuks = Noutbuk.objects.all()
    context = {'noutbuks': noutbuks}

    return render(request, 'list.html', context=context)


def get_noutbuks_info(request, pk):
    try:
        noutbuk = Noutbuk.objects.get(id=pk)
        context = {'noutbuk': noutbuk}
    except Exception as e:
        raise e
    return render(request, 'detail.html', context=context)

