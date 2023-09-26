from django.shortcuts import render, redirect
from .models import Supplier, Product, Car, Shop
from django.contrib.auth import authenticate, login, logout

# Loginpage
def loginview(request):
    return render (request, "loginpage.html")

# Login action
def login_action(request):
    user = request.POST['username']
    passw = request.POST['password']
    # Löytyykö kyseistä käyttäjää?
    user = authenticate(username = user, password = passw)
    #Jos löytyy:
    if user:
        # Kirjataan sisään
        login(request, user)
        # Tervehdystä varten context
        context = {'name': user.first_name}
        # Kutsutaan suoraan landingview.html
        return render(request,'landingpage.html',context)
    # Jos ei kyseistä käyttäjää löydy
    else:
        return render(request, 'loginerror.html')


# Logout action
def logout_action(request):
    logout(request)
    return render(request, 'loginpage.html')


# Product views
def productlistview(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        productlist = Product.objects.all()
        supplierlist = Supplier.objects.all()
        carslist = Car.objects.all()
        shoplist = Shop.objects.all()
        context = {'products': productlist, 'suppliers': supplierlist, 'cars': carslist, 'shops' : shoplist}
        return render (request,"productlist.html",context)


def addproduct(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        a = request.POST['productname']
        b = request.POST['packagesize']
        c = request.POST['unitprice']
        d = request.POST['unitsinstock']
        e = request.POST['supplier']
    
    Product(productname = a, packagesize = b, unitprice = c, unitsinstock = d, supplier = Supplier.objects.get(id = e)).save()
    return redirect(request.META['HTTP_REFERER'])

def confirmdeleteproduct(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        product = Product.objects.get(id = id)
        context = {'product': product}
        return render (request,"confirmdelprod.html",context)


def deleteproduct(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        Product.objects.get(id = id).delete()
        return redirect(productlistview)


def edit_product_get(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        product = Product.objects.get(id = id)
        context = {'product': product}
        return render (request,"edit_product.html",context)


def edit_product_post(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        item = Product.objects.get(id = id)
        item.unitprice = request.POST['unitprice']
        item.unitsinstock = request.POST['unitsinstock']
        item.save()
        return redirect(productlistview)


def products_filtered(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        productlist = Product.objects.all()
        filteredproducts = productlist.filter(supplier = id)
        context = {'products': filteredproducts}
        return render (request,"productlist.html",context)



# Supplier views
def supplierlistview(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        supplierlist = Supplier.objects.all()
        context = {'suppliers': supplierlist}
        return render (request,"supplierlist.html",context)


def addsupplier(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        a = request.POST['companyname']
        b = request.POST['contactname']
        c = request.POST['address']
        d = request.POST['phone']
        e = request.POST['email']
        f = request.POST['country']
        Supplier(companyname = a, contactname = b, address = c, phone = d, email = e, country = f).save()
        return redirect(request.META['HTTP_REFERER'])


def searchsuppliers(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        search = request.POST['search']
        filtered = Supplier.objects.filter(companyname__icontains=search)
        context = {'suppliers': filtered}
        return render (request,"supplierlist.html",context)

#Car views
def carlistview(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        carslist = Car.objects.all()
        context = {'cars': carslist}
        return render (request,"carlist.html",context)


def addcar(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        a = request.POST['companyname']
        b = request.POST['carname']
        c = request.POST['carmodel']
        d = request.POST['drivenkm']
        Car(companyname = a, carname = b, carmodel = c, drivenkm = d).save()
        return redirect(request.META['HTTP_REFERER'])


def searchcars(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        search = request.POST['search']
        filtered = Car.objects.filter(companyname__icontains=search)
        context = {'cars': filtered}
        return render (request,"carlist.html",context)
    

#Shop views
def shoplistview(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        shopslist = Shop.objects.all()
        context = {'shops': shopslist}
        return render (request,"shoplist.html",context)


def addshop(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        a = request.POST['companyname']
        b = request.POST['shoptown']
        c = request.POST['shopaddress']
        Shop(companyname = a, shoptown = b, shopaddress = c).save()
        return redirect(request.META['HTTP_REFERER'])


def searchshops(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        search = request.POST['search']
        filtered = Shop.objects.filter(companyname__icontains=search)
        context = {'shops': filtered}
        return render (request,"shoplist.html",context)



