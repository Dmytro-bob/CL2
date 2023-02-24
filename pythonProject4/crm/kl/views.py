from django.shortcuts import render, redirect
from .models import listofcompanies
from .forms import listofcompaniesForm
def index(request):
    return render(request, 'kl/index.html')


def compani(request):
    list = listofcompanies.objects.all()
    return render(request, 'kl/compani.html', {'title':'Компанії', 'list': list })


def kanban(request):
    return render(request, 'kl/kanban.html')


def events(request):
    return render(request, 'kl/events.html')


def customers(request):
    return render(request, 'kl/customers.html')


def service(request):
    return render(request, 'kl/service.html')


def cash(request):
    return render(request, 'kl/cash.html')


def recruiting(request):
    return render(request, 'kl/recruiting.html')


def newcompani(request):
    if request.method == "POST":
        form = listofcompaniesForm(request.POST)
        return redirect('compani')
    form = listofcompaniesForm()
    context = {
        'form': form
    }
    return render(request, 'kl/newcompani.html', context)