from django.forms import ModelForm
from django import forms
from mainapp.models import *
from bootstrap_datepicker_plus import DateTimePickerInput


class TaxSlabForm(ModelForm):
    class Meta:
        model = TaxSlab
        fields = '__all__'


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = '__all__'


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class FirmForm(ModelForm):
    class Meta:
        model = Firm
        fields = '__all__'


class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'
        widgets = {
            'entry_time': DateTimePickerInput(),  # default date-format %m/%d/%Y will be used
        }


class InvoiceItemForm(ModelForm):
    class Meta:
        model = InvoiceItem
        fields = '__all__'
