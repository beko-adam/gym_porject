from django.shortcuts import render
from members.models import  Mumber
# Create your views here.
def index_(request):
       all_mum_ = Mumber.objects.all()
   

       return render(request, './mumber_/index.html', {'all_mum_': all_mum_ })


def End_sub(request, id):

       all_mum = Mumber.objects.get(id=id)
       
       

       return render(request, './mumber_/detiles.html', {'all_mum':all_mum })

