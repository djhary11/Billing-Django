from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from mainapp.decorators import unauthenticated_user
from mainapp.forms import TaxSlabForm, ServiceForm, CustomerForm, FirmForm, InvoiceForm, InvoiceItemForm
from mainapp.models import TaxSlab, Service, Customer, Firm, Invoice, InvoiceItem
from indicnum2words.num_to_word import num_to_word


@unauthenticated_user
def loginPage(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR Password Invalid.')
    return render(request, 'mainapp/login.html')


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    context = {}
    return render(request, 'mainapp/home.html', context)


@login_required(login_url='login')
def tax_slab_index(request):
    tax_slabs = TaxSlab.objects.all()
    context = {'tax_slabs': tax_slabs}
    return render(request, 'mainapp/TaxSlab/index.html', context)


@login_required(login_url='login')
def tax_slab_delete(request, tax_slab_id):
    try:
        tax_slab = TaxSlab.objects.get(id=tax_slab_id)
        tax_slab.delete()
        messages.success(request, "Tax Slab deleted Successfully")
    except:
        messages.warning(request, "Unable to delete Tax Slab")
    return redirect('tax_slab_index')


@login_required(login_url='login')
def tax_slab_add(request):
    form = TaxSlabForm()
    if request.method == 'POST':
        form = TaxSlabForm(request.POST)
        if form.is_valid():
            form.save()
            form = TaxSlabForm()
            messages.success(request, "Tax Slab added Successfully")
        else:
            error_string = ' '.join([' '.join(x for x in l) for l in list(form.errors.values())])
            messages.warning(request, "Unable to add Tax Slab, " + error_string)
    context = {'form': form}
    return render(request, 'mainapp/TaxSlab/add.html', context)


@login_required(login_url='login')
def tax_slab_edit(request, tax_slab_id):
    tax_slab = TaxSlab.objects.get(id=tax_slab_id)
    form = TaxSlabForm(instance=tax_slab)
    if request.method == 'POST':
        form = TaxSlabForm(request.POST, instance=tax_slab)
        if form.is_valid():
            form.save()
            form = TaxSlabForm()
            messages.success(request, "Tax Slab updated Successfully")
            return redirect('tax_slab_index')
        else:
            error_string = ' '.join([' '.join(x for x in l) for l in list(form.errors.values())])
            messages.warning(request, "Unable to update Tax Slab, " + error_string)
    context = {'form': form}
    return render(request, 'mainapp/TaxSlab/add.html', context)


@login_required(login_url='login')
def service_index(request):
    services = Service.objects.all()
    context = {'services': services}
    return render(request, 'mainapp/Service/index.html', context)


@login_required(login_url='login')
def service_add(request):
    form = ServiceForm()
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            form = ServiceForm()
            messages.success(request, "Service added Successfully")
        else:
            error_string = ' '.join([' '.join(x for x in l) for l in list(form.errors.values())])
            messages.warning(request, "Unable to add Service, " + error_string)
    context = {'form': form}
    return render(request, 'mainapp/Service/add.html', context)


@login_required(login_url='login')
def service_edit(request, service_id):
    service = Service.objects.get(id=service_id)
    form = ServiceForm(instance=service)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, "Service added Successfully")
            return redirect('service_index')
        else:
            error_string = ' '.join([' '.join(x for x in l) for l in list(form.errors.values())])
            messages.warning(request, "Unable to add Service, " + error_string)
    context = {'form': form}
    return render(request, 'mainapp/Service/add.html', context)


@login_required(login_url='login')
def service_delete(request, service_id):
    try:
        service = Service.objects.get(id=service_id)
        service.delete()
        messages.success(request, "Service deleted Successfully")
    except:
        messages.warning(request, "Unable to delete Service")
    return redirect('service_index')


@login_required(login_url='login')
def customer_index(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'mainapp/Customer/index.html', context)


@login_required(login_url='login')
def customer_add(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            form = CustomerForm()
            messages.success(request, "Customer added Successfully")
        else:
            error_string = ' '.join([' '.join(x for x in l) for l in list(form.errors.values())])
            messages.warning(request, "Unable to add Customer, " + error_string)
    context = {'form': form}
    return render(request, 'mainapp/Customer/add.html', context)


@login_required(login_url='login')
def customer_edit(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer edited Successfully")
            return redirect('customer_index')
        else:
            error_string = ' '.join([' '.join(x for x in l) for l in list(form.errors.values())])
            messages.warning(request, "Unable to edit Customer, " + error_string)
    context = {'form': form}
    return render(request, 'mainapp/Customer/add.html', context)


@login_required(login_url='login')
def customer_delete(request, customer_id):
    try:
        customer = Customer.objects.get(id=customer_id)
        customer.delete()
        messages.success(request, "Customer deleted Successfully")
    except:
        messages.warning(request, "Unable to delete Customer")
    return redirect('customer_index')


@login_required(login_url='login')
def firm_index(request):
    firms = Firm.objects.all()
    context = {'firms': firms}
    return render(request, 'mainapp/Firm/index.html', context)


@login_required(login_url='login')
def firm_add(request):
    form = FirmForm()
    if request.method == 'POST':
        form = FirmForm(request.POST)
        if form.is_valid():
            form.save()
            form = FirmForm()
            messages.success(request, "Firm added Successfully")
        else:
            error_string = ' '.join([' '.join(x for x in l) for l in list(form.errors.values())])
            messages.warning(request, "Unable to add Firm, " + error_string)
    context = {'form': form}
    return render(request, 'mainapp/Firm/add.html', context)


@login_required(login_url='login')
def firm_edit(request, firm_id):
    firm = Firm.objects.get(id=firm_id)
    form = FirmForm(instance=firm)
    if request.method == 'POST':
        form = FirmForm(request.POST, instance=firm)
        if form.is_valid():
            form.save()
            messages.success(request, "Firm edited Successfully")
            return redirect('firm_index')
        else:
            error_string = ' '.join([' '.join(x for x in l) for l in list(form.errors.values())])
            messages.warning(request, "Unable to edit Firm, " + error_string)
    context = {'form': form}
    return render(request, 'mainapp/Firm/add.html', context)


@login_required(login_url='login')
def firm_delete(request, firm_id):
    try:
        firm = Firm.objects.get(id=firm_id)
        firm.delete()
        messages.success(request, "firm deleted Successfully")
    except:
        messages.warning(request, "Unable to delete firm")
    return redirect('firm_index')


# support function not view
def invoice_calc_total(invoice_id):
    invoice = Invoice.objects.get(id=invoice_id)
    sub_total = InvoiceItem.objects.filter(invoice=invoice).aggregate(Sum('amount'))['amount__sum']
    gst_slab = invoice.tax_slab.value
    gst_amount = sub_total * (gst_slab / 100)
    total_with_gst = sub_total + gst_amount
    invoice.sub_total = sub_total
    invoice.gst_amount = gst_amount
    invoice.total_with_gst = total_with_gst
    invoice.save()


@login_required(login_url='login')
def invoice_create(request):
    form = InvoiceForm()
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.save()
            messages.success(request, "Invoice created successfully, now add items")
            return redirect('invoice_add_item', entry.id)
        else:
            error_string = ' '.join([' '.join(x for x in l) for l in list(form.errors.values())])
            messages.warning(request, "Unable to create Invoice, " + error_string)
    context = {'form': form}
    return render(request, 'mainapp/Invoice/create.html', context)


@login_required(login_url='login')
def invoice_add_item(request, invoice_id):
    invoice = Invoice.objects.get(id=invoice_id)
    form = InvoiceItemForm()
    if request.method == 'POST':
        form = InvoiceItemForm(request.POST)
        if form.is_valid():
            item_entry = form.save(commit=False)
            item_entry.invoice = invoice
            item_entry.amount = item_entry.quantity * item_entry.rate_per_unit
            item_entry.save()
            invoice_calc_total(invoice_id)
            messages.success(request, "Item added to invoice")
            form = InvoiceItemForm()
        else:
            error_string = ' '.join([' '.join(x for x in l) for l in list(form.errors.values())])
            messages.warning(request, "Unable to add Item to invoice, " + error_string)
    invoice_items = InvoiceItem.objects.filter(invoice=invoice)
    context = {'form': form, 'invoice_items': invoice_items, 'invoice': invoice}
    return render(request, 'mainapp/Invoice/add_item.html', context)


@login_required(login_url='login')
def invoice_index(request):
    invoices = Invoice.objects.all()
    context = {'invoices': invoices}
    return render(request, 'mainapp/Invoice/index.html', context)


@login_required(login_url='login')
def invoice_view(request, invoice_id):
    invoice = Invoice.objects.get(id=invoice_id)
    total_in_num = round(invoice.total_with_gst)
    total_amount_in_words_en = num_to_word(total_in_num, lang="en")
    total_amount_in_words_hi = num_to_word(total_in_num, lang="hi")
    context = {'invoice': invoice, 'total_amount_in_words_en': total_amount_in_words_en,
               'total_amount_in_words_hi': total_amount_in_words_hi, 'total_in_num': total_in_num}
    return render(request, 'mainapp/Invoice/view.html', context)


@login_required(login_url='login')
def invoice_edit(request, invoice_id):
    invoice = Invoice.objects.get(id=invoice_id)
    form = InvoiceForm(instance=invoice)
    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            form.save()
            invoice_calc_total(invoice.id)
            messages.success(request, "Invoice updated successfully, now manage items")
            return redirect('invoice_add_item', invoice.id)
        else:
            error_string = ' '.join([' '.join(x for x in l) for l in list(form.errors.values())])
            messages.warning(request, "Unable to update Invoice, " + error_string)
    context = {'form': form}
    return render(request, 'mainapp/Invoice/create.html', context)


@login_required(login_url='login')
def invoice_item_delete(request, invoice_item_id):
    try:
        invoice_item = InvoiceItem.objects.get(id=invoice_item_id)
        invoice_item.delete()
        messages.success(request, "Invoice Item deleted Successfully")
    except:
        messages.warning(request, "Unable to delete Invoice Item")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='login')
def invoice_delete(request, invoice_id):
    try:
        invoice = Invoice.objects.get(id=invoice_id)
        invoice.delete()
        messages.success(request, "Invoice deleted Successfully")
    except:
        messages.warning(request, "Unable to delete Invoice")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))