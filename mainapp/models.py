from django.db import models


# Create your models here.


class TaxSlab(models.Model):
    value = models.DecimalField(max_digits=4, decimal_places=2, default=0.00, blank=False, null=False)

    def __str__(self):
        return str(self.value) + " % "


class Service(models.Model):
    name = models.CharField(max_length=25, null=False, blank=False, unique=True)

    def __str__(self):
        return str(self.name)


class Firm(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    address = models.TextField(max_length=300, null=False, blank=False)
    state = models.CharField(max_length=50, null=False, blank=False)
    mobile_number = models.CharField(max_length=25, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=True, default="")
    bank_ac_name = models.CharField(max_length=50, null=False, blank=True, default="")
    bank_name = models.CharField(max_length=50, null=False, blank=True, default="")
    bank_branch_address = models.TextField(max_length=300, null=False, blank=True, default="")
    bank_ac_number = models.CharField(max_length=30, null=False, blank=True, default="")
    bank_ifsc_code = models.CharField(max_length=30, null=False, blank=True, default="")
    gstin_number = models.CharField(max_length=30, null=False, blank=True, default="")
    footer_text = models.TextField(max_length=300, null=False, blank=True, default=" ")

    def __str__(self):
        return str(self.name)


class Customer(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    address = models.TextField(max_length=300, null=False, blank=False)
    state = models.CharField(max_length=50, null=False, blank=False)
    mobile_number = models.CharField(max_length=25, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=True, default="")
    bank_ac_name = models.CharField(max_length=50, null=False, blank=True, default="")
    bank_name = models.CharField(max_length=50, null=False, blank=True, default="")
    bank_branch_address = models.TextField(max_length=300, null=False, blank=True, default="")
    bank_ac_number = models.CharField(max_length=30, null=False, blank=True, default="")
    bank_ifsc_code = models.CharField(max_length=30, null=False, blank=True, default="")
    gstin_number = models.CharField(max_length=30, null=False, blank=True, default="")

    def __str__(self):
        return str(self.name)


class Invoice(models.Model):
    firm = models.ForeignKey(Firm, on_delete=models.PROTECT, blank=False, null=False)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, blank=False, null=False)
    tax_slab = models.ForeignKey(TaxSlab, on_delete=models.PROTECT, blank=False, null=False)
    challan_nos = models.CharField(max_length=150, null=False, blank=True, default=" ")
    entry_time = models.DateTimeField(blank=False, null=False)
    item_description = models.CharField(max_length=200, null=False, blank=True, default=" ")
    sub_total = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=False, default=0)
    gst_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=False, default=0)
    total_with_gst = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=False, default=0)

    def __str__(self):
        return str(self.id) + " | " + str(self.customer) + " | " + str(self.total_with_gst)


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, blank=True, null=True)
    service = models.ForeignKey(Service, on_delete=models.PROTECT, blank=False, null=False)
    description = models.CharField(max_length=200, null=False, blank=True, default=" ")
    quantity = models.IntegerField(blank=False, null=False)
    rate_per_unit = models.DecimalField(max_digits=12, decimal_places=2, blank=False, null=False, default=0)
    amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=False, default=0)
