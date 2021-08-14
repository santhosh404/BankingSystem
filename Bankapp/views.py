from django.shortcuts import render
from . models import *
from django.http import HttpResponseRedirect
from django.urls import reverse



def Index(request):
    return render(request, 'index.html')


def Customer_Details(request):
    global indcustomer
    all_customers = Customers.objects.all()
    if request.method == "POST":
        global indcustomer
        customer = request.POST['customer']
        indcustomer = Customers.objects.filter(id=customer)[0]
        return HttpResponseRedirect(reverse('indcustomer'))
    return render(request, 'customers.html', {'customers':all_customers})

def Induival_Customer(request):
    global trans_name
    global trans_id
    if request.method == 'POST':
        trans_name = request.POST['transfername']
        trans_id = indcustomer.id
        return HttpResponseRedirect(reverse('transaction'))
    return render(request, 'indcustomer.html' , {'incustomer':indcustomer})


def Transact(request):
    all_customers = Customers.objects.all()
    if request.method == 'POST':
        print(request.POST)
        from_id = request.POST.get('fromid', False)
        to_id = request.POST.get('toid', False)
        amount = request.POST['amount']
        
        from_model = Customers.objects.filter(id=int(from_id))[0]
        from_amt = from_model.bal
        to_model = Customers.objects.filter(id=int(to_id))[0]
        to_amt = to_model.bal
        if (from_amt - int(amount) < 0):
            return render(request, 'transaction.html', {'customers':all_customers, 'error':'Insufficient Balance'})
        
       
        else:
            to_model.bal = round(to_amt + int(amount),2) 
            to_model.save()
            from_model.bal = round(from_amt - int(amount),2) 
            from_model.save()
            t = Transactions(from_name=from_model.name, to_name=to_model.name, trans_amt=amount)
            t.save()

            return HttpResponseRedirect(reverse('history'))

        return render(request, 'transaction.html', {'customers':all_customers})

    return render(request, 'transaction.html', {'customers':all_customers, 'trans_name':trans_name, 'trans_id':trans_id})


def History(request):
    hist = Transactions.objects.all()
    return render(request, 'history.html', {'hist':hist})