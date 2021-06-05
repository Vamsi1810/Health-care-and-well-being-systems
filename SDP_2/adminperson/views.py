from django.shortcuts import render
from pharmacy.models import MedicineOrder, Pharmacy
from doctor.models import Consult, Doctor
from customer.models import Patient

# Create your views here.
def AdminHomePage(request):
    medor=MedicineOrder.objects.all()
    data1=[0,0,0,0,0,0,0,0,0,0,0,0]
    for i in medor:
        my_mon = i.date.strftime("%m")
        p=int(my_mon)
        data1[p-1]+=1
    data2=[0,0,0,0,0,0,0,0,0,0,0,0]
    con=Consult.objects.all()
    for i in con:
        my_mon = i.date.strftime("%m")
        p=int(my_mon)
        data2[p-1]+=1
    labels = ['Patients','Doctors','Pharmacist']
    data = []

    c=0
    pat=Patient.objects.all()
    for i in pat:
        c=c+1
    data.append(c)
    c=0
    doc=Doctor.objects.filter(assign=True)
    for d in doc:
        c+=1
    data.append(c)
    c=0
    pha=Pharmacy.objects.filter(assign=True)
    for p in pha:
        c+=1
    data.append(c)
    return render(request,'adminhome.html',{'data1':data1,'data2':data2,'labels': labels,'data3': data})
# from django.views.generic import TemplateView
# from chartjs.views.lines import BaseLineChartView


# class LineChartJSONView(BaseLineChartView):
#     def get_labels(self):
#         """Return 7 labels for the x-axis."""
#         return ["January", "February", "March", "April", "May", "June", "July"]

#     def get_providers(self):
#         """Return names of datasets."""
#         return ["Central", "Eastside", "Westside"]

#     def get_data(self):
#         """Return 3 datasets to plot."""

#         return [[75, 44, 92, 11, 44, 95, 35],
#                 [41, 92, 18, 3, 73, 87, 92],
#                 [87, 21, 94, 3, 90, 13, 65]]


# line_chart = TemplateView.as_view(template_name='line_chart.html')
# line_chart_json = LineChartJSONView.as_view()

def pie_chart(request):
    labels = ['Patients','Doctors','Pharmacist']
    data = []

    c=0
    pat=Patient.objects.all()
    for i in pat:
        c=c+1
    data.append(c)
    c=0
    doc=Doctor.objects.filter(assign=True)
    for d in doc:
        c+=1
    data.append(c)
    c=0
    pha=Pharmacy.objects.filter(assign=True)
    for p in pha:
        c+=1
    data.append(c)
    return render(request, 'pie_chart.html', {
        'labels': labels,
        'data': data,
    })