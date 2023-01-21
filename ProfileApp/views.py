from django.shortcuts import render

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

    product = ['บุรุษเต้าหู้สะท้านภพ', 450.00, 'book_1.gif']
    products.append(product)
    product = ['ก็จะดื้อ (2 เล่มจบ)', 559.00, 'book_2.gif']
    products.append(product)
    product = ['วันๆ ของจิ้งจอกลูกสองก็แบบนี้แหละ!', 429.00, 'book_3.gif']
    products.append(product)
    product = ['A piece of cake', 289.00, 'book_4.gif']
    products.append(product)
    product = ['ทีเร็กซ์จะไม่ดื้อ', 399.00, 'book_5.gif']
    products.append(product)
    product = ['บุรุษเต้าหู้สะท้านภพ', 450.00, 'book_6.gif']
    products.append(product)
    product = ['นับสิบจะจูบ (2 เล่มจบ)', 680.00, 'book_7.gif']
    products.append(product)
    product = ['เกิดใหม่เป็นตัวร้ายผู้รักสงบ', 379.00, 'book_8.gif']
    products.append(product)
    product = ['อัยย์หลงไน๋', 300.00, 'book_9.gif']
    products.append(product)
    product = ['Real Alpha (2 เล่มจบ)', 518.00, 'book_10.gif']
    products.append(product)

    context = {'showID': showID, 'showName': showName, 'showAddress': showAddress, 'showTel': showTel,
               'showGender': showGender, 'showBirthday': showBirthday, 'showWeight': showWeight,
               'showHeight': showHeight, 'showStatus': showStatus, 'showSchool': showSchool, 'products': products}

    return render(request, 'showMyData.html', context)
