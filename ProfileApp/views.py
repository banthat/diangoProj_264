from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def home(request):
    return render(request, 'home.html')


def personal(request):
    return render(request, 'personal.html')


def educational(request):
    return render(request, 'educational.html')


def interests(request):
    return render(request, 'interests.html')


def sell(request):
    return render(request, 'sell.html')


def rolemodel(request):
    return render(request, 'rolemodel.html')


def showMyData(request):

    showID = "65342310264-8"
    showName = "นายบัณทัต อุประ"
    showAddress = "46 หมู่ 8 ตำบลแคนใหญ่ อำเภอเมืองร้อยเอ็ด จังหวัดร้อยเอ็ด 45000"
    showTel = "0855129238"
    showGender = "ชาย"
    showBirthday = "12 กุมภาพันธ์ 2545"
    showWeight = 45
    showHeight = 169
    showStatus = "นักศึกษา"
    showSchool = "มหาวิทยาลัยเทคโนโลยีราชมงคลอีสาน วิทยาเขตขอนแก่น"

    products = []

    product = ['บุรุษเต้าหู้สะท้านภพ', 450.00, '../../static/image/book_1.gif']
    products.append(product)
    product = ['ก็จะดื้อ (2 เล่มจบ)', 559.00, '../../static/image/book_2.gif']
    products.append(product)
    product = ['วันๆ ของจิ้งจอกลูกสองก็แบบนี้แหละ!', 429.00, '../../static/image/book_3.gif']
    products.append(product)
    product = ['A piece of cake', 289.00, '../../static/image/book_4.gif']
    products.append(product)
    product = ['ทีเร็กซ์จะไม่ดื้อ', 399.00, '../../static/image/book_5.gif']
    products.append(product)
    product = ['บุรุษเต้าหู้สะท้านภพ', 450.00, '../../static/image/book_6.gif']
    products.append(product)
    product = ['นับสิบจะจูบ (2 เล่มจบ)', 680.00, '../../static/image/book_7.gif']
    products.append(product)
    product = ['เกิดใหม่เป็นตัวร้ายผู้รักสงบ', 379.00, '../../static/image/book_8.gif']
    products.append(product)
    product = ['ผมไม่เป็น(โอเมก้า)ของคุณหรอก! (3 เล่มจบ)', 948.00, '../../static/image/book_13.gif']
    products.append(product)
    product = ['Real Alpha (2 เล่มจบ)', 518.00, '../../static/image/book_10.gif']
    products.append(product)

    context = {'showID': showID, 'showName': showName, 'showAddress': showAddress, 'showTel': showTel,
               'showGender': showGender, 'showBirthday': showBirthday, 'showWeight': showWeight,
               'showHeight': showHeight, 'showStatus': showStatus, 'showSchool': showSchool, 'products': products}

    return render(request, 'showMyData.html', context)

lstOurProduct = []

from ProfileApp.models import *
from ProfileApp.forms import *

def listProduct(request):
    context = {'products': lstOurProduct}
    return render(request, 'listProduct.html', context)

def inputProduct(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            id = form.get('id')
            brand = form.get('brand')
            model = form.get('model')
            color = form.get('color')
            type = form.get('type')
            price = form.get('price')

            if price <= 5000:
                warranty = 1
            elif price <= 10000:
                warranty = 2
            elif price <= 50000:
                warranty = 3
            else:
                warranty = 4

            vat = price * 0.07
            net = price + vat
            pd = Product(id, brand, model, color, type, price, warranty, vat, net)
            lstOurProduct.append(pd)
            return redirect('listProduct')
        else:
            form = ProductForm(form)
    else:
        form = ProductForm()
        context = {'form': form}
        return render(request, 'inputProduct.html', context)

def showGoodsList(request):
    goods = Goods.objects.all()
    context = {'goods': goods}
    return render(request, 'Product/showGoodsList.html', context)

def showGoodsOne(request, gid):
    goods = Goods.objects.get(gid=gid)
    context = {'goods': goods}
    return render(request, 'Product/showGoodsOne.html', context)

from django.contrib import messages

def newGoods(request):
    if request.method == "POST":
        form = GoodsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'บันทึกข้อมูลสินค้าสำเร็จแล้ว')
            return redirect('showGoodsList')
        else:
            goods = Goods.objects.get(gid=form.gid)
            if goods:
                messages.add_message(request, messages.WARNING, 'รหัสสินค้าซ้ำกับกับที่มีอยู่แล้ว')
            else:
                messages.add_message(request, messages.WARNING, 'ข้อมูลไม่ถูกต้อง/ไม่สมบูรณ์ ไม่สามารถบันทึกได้')
    else:
        form = GoodsForm()
    context = {'form': form}
    return render(request, 'Product/newGoods.html', context)

from django.shortcuts import get_object_or_404
def updateGoods(request, gid):
    obj = get_object_or_404(Goods, gid=gid)
    form = GoodsForm(request.POST or None, instance=obj)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'ปรับปรุงข้อมูลสินค้าสำเร็จ')
            return redirect('showGoodsList')
        else:
            messages.add_message(request, messages.WARNING, 'ข้อมูลไม่ถูกต้อง/ไม่สามารถปรับปรุงได้')
    form.updateForm()
    context = {'form': form}
    return render(request, 'Product/updateGoods.html', context)

