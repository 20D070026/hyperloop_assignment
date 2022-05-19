from django.shortcuts import render
from django.http import HttpResponse
from .models import ContactDetail

# Create your views here.
def form_view(request):
    return render(request, 'form.html')

def form_data_view(request):
    data = dict(request.POST)
    details = ContactDetail(Name=data['name'][0], Comments=data['comments'][0], Email=data['email'][0], Phone=data['phone'][0], Dept=data['dept'][0], Roll=data['roll'][0], SubA=bool(data.get('aero', [False])[0]), SubC=bool(data.get('controls', [False])[0]), SubE=bool(data.get('electricals', [False])[0]), SubP=bool(data.get('prop', [False])[0]), SubS=bool(data.get('structures', [False])[0]))
    details.save()
    return render(request, "response.html")