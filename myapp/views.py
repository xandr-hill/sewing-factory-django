from django.shortcuts import render, redirect
from .forms import FabricRollForm, CuttingForm, SewingForm, IroningForm, ContactForm
from .models import FabricRoll, Cutting, Sewing, Ironing, Contact
from .models import Sewing
from .models import Ironing

def sewing_reports(request):
    # Получаем все дневные отчеты по пошиву
    sewing_reports = Sewing.objects.all()
    
    # Передаем данные в шаблон
    return render(request, 'sewing_reports.html', {'sewing_reports': sewing_reports})

def ironing_reports(request):
    # Получаем все дневные отчеты по утюгу
    ironing_reports = Ironing.objects.all()
    
    # Передаем данные в шаблон
    return render(request, 'ironing_reports.html', {'ironing_reports': ironing_reports})

def warehouse(request):
    fabric_rolls = FabricRoll.objects.all()
    return render(request, 'warehouse.html', {'fabric_rolls': fabric_rolls})

def cutting(request):
    cuttings = Cutting.objects.all()
    return render(request, 'cutting.html', {'cuttings': cuttings})

def sewing(request):
    sewings = Sewing.objects.all()
    return render(request, 'sewing.html', {'sewings': sewings})

def ironing(request):
    ironings = Ironing.objects.all()
    return render(request, 'ironing.html', {'ironings': ironings})

def contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts.html', {'contacts': contacts})

def login(request):
    # Ваш код авторизации
    return render(request, 'login.html')
