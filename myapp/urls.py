# myapp/urls.py
from django.urls import path
from .views import (
    warehouse, cutting, sewing, ironing, contacts, login,
    fabric_roll_form, cutting_form, sewing_report, ironing_report,
    contact_form, fabric_roll_edit, fabric_roll_delete,
    cutting_edit, cutting_delete, contact_edit, contact_delete,
    sewing_reports, ironing_reports,
)

urlpatterns = [
    path('warehouse/', warehouse, name='warehouse'),
    path('cutting/', cutting, name='cutting'),
    path('sewing/', sewing, name='sewing'),
    path('ironing/', ironing, name='ironing'),
    path('contacts/', contacts, name='contacts'),
    path('login/', login, name='login'),

    # URL-шаблоны для форм
    path('fabric_roll_form/', fabric_roll_form, name='fabric_roll_form'),
    path('cutting_form/', cutting_form, name='cutting_form'),
    path('sewing_report/', sewing_report, name='sewing_report'),
    path('ironing_report/', ironing_report, name='ironing_report'),
    path('contact_form/', contact_form, name='contact_form'),

    # URL-шаблоны для редактирования и удаления
    path('fabric_roll_edit/<int:fabric_roll_id>/', fabric_roll_edit, name='fabric_roll_edit'),
    path('fabric_roll_delete/<int:fabric_roll_id>/', fabric_roll_delete, name='fabric_roll_delete'),
    path('cutting_edit/<int:cutting_id>/', cutting_edit, name='cutting_edit'),
    path('cutting_delete/<int:cutting_id>/', cutting_delete, name='cutting_delete'),
    path('contact_edit/<int:contact_id>/', contact_edit, name='contact_edit'),
    path('contact_delete/<int:contact_id>/', contact_delete, name='contact_delete'),

    # Добавленные URL-шаблоны для отчетов
    path('sewing_reports/', sewing_reports, name='sewing_reports'),
    path('ironing_reports/', ironing_reports, name='ironing_reports'),
]
