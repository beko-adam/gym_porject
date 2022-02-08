from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from .models import Mumber
from .form import Meumber_Form, Meumber_Form_sub
from .filter_ import Mumer_Filter
from django.urls import reverse
import  datetime


# Create your views here.


def all_members(request):


    all_memb = Mumber.objects.all()
    my_filter = Mumer_Filter(request.GET, queryset=all_memb)
    all_memb = my_filter.qs
    paginator = Paginator(all_memb, 6) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    all_memb_ = paginator.get_page(page_number)
    

    ex_date = []
    date_day = datetime.date.today()


    for j in all_memb_:

        date_long = datetime.date.today() - j.data_sub
     
        ex_date.append(date_long.days)
        print(ex_date)
    my_st = zip(all_memb_, ex_date)
    
    context = {
                'all_mem': all_memb_,
                'ex_date':date_day.day,
                'my_st': my_st,
                'my_filter':my_filter
                
                }

    return render(request, './mumber_/home.html', context)





def detalis_members(request, id):

    

    detalis_memb = Mumber.objects.get(id=id)
    date_long = datetime.date.today() - detalis_memb.data_sub
    print( date_long.days, ":::::::::::::::::")
    print( detalis_memb.data_sub, 'hi')
    context = {
        'detalis_memb': detalis_memb,
        'date_long':date_long
              }

    return render(request, './mumber_/detiles.html', context)




def Add_mumber(request):

    if request.method == 'POST':
       form_ = Meumber_Form(request.POST, request.FILES)
       if form_.is_valid():
           my_form = form_.save(commit=False)
           my_form.owner = request.user
           my_form.save()
           return redirect(reverse('member:all_members'))
    else:

        form_ = Meumber_Form( )

    return render(request, './mumber_/Add.html', {'form': form_ })


def Editr_Mumber(request, id):
    edit =Mumber.objects.get(id=id)
    if request.method == 'POST':
        form = Meumber_Form(request.POST, request.FILES, instance=edit)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.owner = request.user
            my_form.save()
            return redirect(reverse('member:all_members'))

    else:
        form = Meumber_Form(instance=edit)

    return render(request, './mumber_/editr.html', {'form': form})



def Editr_Mumber_usb(request, id):
    edit =Mumber.objects.get(id=id)
    if request.method == 'POST':
        form = Meumber_Form_sub(request.POST, request.FILES, instance=edit)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.owner = request.user
            my_form.save()
            return redirect(reverse('member:all_members'))

    else:
        form = Meumber_Form_sub(instance=edit)

    return render(request, './mumber_/Subscribe.html', {'form': form})

def get_404_er(request, exception):

    return render(request, './mumber_/404.html', status=404)
    