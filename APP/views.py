import xlrd
from django.shortcuts import render
from APP.models import MedicineDetails, DealerDetails
from django.db.models import Q
# Create your views here.
from django.http import HttpResponse


def load_homepage(request):
    return render(request,'index.html')

def load_data_from_xls(request):
    import pdb
    pdb.set_trace()
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
    return HttpResponse("data Added Successfully")
