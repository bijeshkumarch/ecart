from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Order, orderUpdate
import math, json
from django.utils.timezone import activate


# Create your views here.


def index(request):
    products = Product.objects.all()
    n = len(products)
    allProd = []
    catProds = Product.objects.values("category", "id")
    cats = {item["category"] for item in catProds}
    for cat in cats:
        prod = Product.objects.filter(category = cat)
        n = len(prod)
        nSlides = n//4 + math.ceil((n%4)/4)
        allProd.append([nSlides, range(1, nSlides), prod])
    allProd.sort(key= lambda x: x[2][0].category)
    param = {"allProd": allProd}
    return render(request, 'shop/index.html', param)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    if request.method=='POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        cont = Contact(name=name, email=email, phone=phone, desc=desc)
        cont.save()
        status = True
        return render(request, "shop/contact.html", {'status':status})
    return render(request, "shop/contact.html")


def tracker(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        order_id = request.POST.get('orderid', '')
        print(email)
        print(order_id)
        try:
            order = Order.objects.filter(email=email, order_id=order_id)
            #print(order)
            if len(order)>0:
                update = orderUpdate.objects.filter(order_id=order_id)
                updates = []
                for item in update:
                    #activate(item.timestamp)
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                response = json.dumps([updates, order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')
    return render(request, "shop/tracker.html")


def search(request):
    return HttpResponse("We are at search")


def productview(request, myid):
    #fetch the product using the id
    product = Product.objects.filter(id = myid)
    return render(request, "shop/productView.html", {"product": product[0], "id": myid})


def checkout(request):
    status = False
    id = 'undefined'
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', 'Not provided') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        pin = request.POST.get('pin', '')
        phone = request.POST.get('phone', '')
        itemJson = request.POST.get('itemsJson', '')
        cost = request.POST.get('cost', 0)
        order = Order(name = name, email=email, address=address, city=city, state=state, zip_code=pin, phone=phone, items_json=itemJson, cost=cost)
        order.save()
        id = order.order_id
        status = True
        #print("order placed", )
        update = orderUpdate(order_id=id, update_desc="Your order has been placed")
        update.save()
        return render(request, 'shop/checkout.html', {'status':status, 'id':id})

    return render(request, 'shop/checkout.html', {'status':status, 'id':id})