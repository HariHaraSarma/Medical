from __future__ import unicode_literals

from django.db import models

# Create your models here.

class PersonDetails(models.Model):
    name = models.CharField(max_length = 20,unique = True)
    phone = models.CharField(max_length = 10,unique = True)
    email_id = models.CharField(max_length = 50,unique = True)
    address = models.CharField(max_length = 100)

    def __unicode__(self):
        return str(self.name)
    
class DealerDetails(models.Model):
    get_dealer_details = models.ForeignKey(PersonDetails)

    #def __unicode__(self):
    #    return str(self.get_dealer_details.name)

class CustomerDetais(models.Model):
    get_dist_details = models.ForeignKey(PersonDetails, default=None)

    #def __unicode__(self):
    #    return str(self.get_dealer_details.name)

class MedicineDetails(models.Model):
    company_name = models.CharField(max_length = 100,unique = True)
    item_name = models.CharField(max_length = 100,unique = True)
    batch_no = models.IntegerField(unique = True)
    mfg_date = models.DateField()
    exp_date = models.DateField()
    org_price = models.DecimalField(max_digits=5, decimal_places=5)
    margin_price = models.DecimalField(max_digits=5, decimal_places=5, null=True, default=0)
    description = models.CharField(max_length = 200)
    present_stock = models.IntegerField()
    dealer = models.ForeignKey(DealerDetails)

    def __unicode__(self):
        return str(self.item_name)




    
    
    
    
    
