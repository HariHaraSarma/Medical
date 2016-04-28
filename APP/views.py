import xlrd
from django.shortcuts import render_to_response, render
from APP.models import MedicineDetails, DealerDetails
from django.db.models import Q
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from django.template import RequestContext


def load_homepage(request):
    return render(request,'index.html')

def load_data_from_xls(request):
    wb = xlrd.open_workbook("F:\Stock_Details.xls")
    # get the first worksheet
    first_sheet = wb.sheet_by_index(0)
    # read a row
    for row in range(1, first_sheet.nrows):
        # Read each row and insert those values into DB.
        try:
            obj = MedicineDetails.objects.get(Q(item_name=first_sheet.cell(row, 1).value) & Q(batch_no=int(first_sheet.cell(row, 2).value)))
            obj.present_stock = obj.present_stock + int(first_sheet.cell(row, 8).value)
            obj.save()
        except:
            obj = MedicineDetails(company_name=first_sheet.cell(row, 0).value,
                                  item_name=first_sheet.cell(row, 1).value,
                                  batch_no=int(first_sheet.cell(row, 2).value),
                                  mfg_date=xlrd.xldate.xldate_as_datetime(first_sheet.cell(row, 3).value, wb.datemode).date(),
                                  exp_date=xlrd.xldate.xldate_as_datetime(first_sheet.cell(row, 4).value, wb.datemode).date(),
                                  org_price=float(first_sheet.cell(row, 5).value),
                                  margin_price=float(first_sheet.cell(row, 6).value),
                                  description=first_sheet.cell(row, 7).value,
                                  present_stock=int(first_sheet.cell(row, 8).value),
                                  dealer=DealerDetails.objects.get(get_dealer_details__name=first_sheet.cell(row, 9).value))
            obj.save()
    return HttpResponse("data Added Successfully", RequestContext(request))


def load_add_item_page(request):
    dealer_names = [obj.get_dealer_details.name for obj in DealerDetails.objects.all()]
    return render_to_response('load_add_an_item.html', {'dealer_names': dealer_names}, context_instance=RequestContext(request))

def add_new_item(request):
    data = request.POST
    try:
        obj = MedicineDetails.objects.get(Q(item_name=data.get('item_name')) & Q(batch_no=int(data.get('batch_number'))))
        obj.present_stock = obj.present_stock + int(data.get('quanity'))
        obj.save()
    except:
        obj = MedicineDetails(company_name=data.get('company'),
                      item_name=data.get('item_name'),
                      batch_no=int(data.get('batch_number')),
                      mfg_date=datetime.strptime(str(data.get('manf_date')) , '%Y-%m-%d'),
                      exp_date=datetime.strptime(str(data.get('exp_date')) , '%Y-%m-%d'),
                      org_price=float(data.get('ppu')),
                      margin_price=float(data.get('margin')),
                      description=data.get('desc'),
                      present_stock=int(data.get('quantity')),
                      dealer=DealerDetails.objects.get(get_dealer_details__name=str(data.get('dealer_name'))))
        obj.save()
    
    return HttpResponse("Added one recored Successfully", RequestContext(request))

def search_page(request):
    return render(request, 'search.html')

def search_for_item(request):
    import pdb
    pdb.set_trace()
    data = request.GET
    if str(data.get('it_name')) and str(data.get('bt_no')) and not str(data.get('comp_name')):
        try:
            objs = MedicineDetails.objects.filter(Q(item_name=str(data.get('it_name'))) & Q(batch_no=int(str(data.get('bt_no')))))
        except:
            return HttpResponseRedirect('/')
    elif str(data.get('it_name')) and not str(data.get('bt_no')) and not str(data.get('comp_name')):
        try:
            objs = MedicineDetails.objects.filter(item_name=str(data.get('it_name')))
        except:
            return HttpResponseRedirect('/')
    elif str(data.get('bt_no')) and not str(data.get('it_name')) and not str(data.get('comp_name')):
        try:
            objs = MedicineDetails.objects.filter(batch_no=int(str(data.get('bt_no'))))
        except:
            return HttpResponseRedirect('/')
    elif str(data.get('comp_name')) and not str(data.get('bt_no')) and not str(data.get('it_name')):
        try:
            objs = MedicineDetails.objects.filter(company_name=str(data.get('comp_name')))
        except:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

    if len(objs) > 0:
      return render_to_response('show.html',
                                {'objs': objs},
                                context_instance=RequestContext(request))
    else:
      return HttpResponseRedirect('/')

# 'dealer_name': obj.dealer.get_dealer_details.name},

def show_complete_stock(request):
    objs=MedicineDetails.objects.all()
    return render to response('show.html',{'objs': objs},
                              context_instance=RequestContext(request))
