from django.contrib import admin
from django.urls import path, include
from mainapp import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"), 
    path('tax-slab/', views.tax_slab_index, name="tax_slab_index"),
    path('tax-slab/add/', views.tax_slab_add, name="tax_slab_add"),
    path('tax-slab/edit/<str:tax_slab_id>/', views.tax_slab_edit, name="tax_slab_edit"),
    path('tax-slab/delete/<str:tax_slab_id>/', views.tax_slab_delete, name="tax_slab_delete"),

    path('service/', views.service_index, name="service_index"),
    path('service/add/', views.service_add, name="service_add"),
    path('service/edit/<str:service_id>/', views.service_edit, name="service_edit"),
    path('service/delete/<str:service_id>/', views.service_delete, name="service_delete"),

    path('customer/', views.customer_index, name="customer_index"),
    path('customer/add/', views.customer_add, name="customer_add"),
    path('customer/edit/<str:customer_id>/', views.customer_edit, name="customer_edit"),
    path('customer/delete/<str:customer_id>/', views.customer_delete, name="customer_delete"),

    path('firm/', views.firm_index, name="firm_index"),
    path('firm/add/', views.firm_add, name="firm_add"),
    path('firm/edit/<str:firm_id>/', views.firm_edit, name="firm_edit"),
    path('firm/delete/<str:firm_id>/', views.firm_delete, name="firm_delete"),

    path('invoice/', views.invoice_index, name="invoice_index"),
    path('invoice/create/', views.invoice_create, name="invoice_create"),
    path('invoice/add-item/<str:invoice_id>/', views.invoice_add_item, name="invoice_add_item"),
    path('invoice/delete-item/<str:invoice_item_id>/', views.invoice_item_delete, name="invoice_delete_item"),
    path('invoice/view/<str:invoice_id>/', views.invoice_view, name="invoice_view"),
    path('invoice/edit/<str:invoice_id>/', views.invoice_edit, name="invoice_edit"),
    path('invoice/delete/<str:invoice_id>/', views.invoice_delete, name="invoice_delete"),

]