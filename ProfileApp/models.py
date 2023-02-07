from django.db import models
class Product:
    def __init__(self, id, brand, model, color, type, price, warranty, vat, net):
        self.id = id
        self.brand = brand
        self.model = model
        self.color = color
        self.type = type
        self.price = price
        self.warranty = warranty
        self.vat = vat
        self.net = net

    def __str__(self):
        return "ID.{}, Name.{}, Brand.{}, Color.{}, Warranty.{}, Price.{}, Warranty.{}, Vat.{}, Net.{}" \
            .format(self.id, self.brand, self.model, self.color, self.warranty, self.price,
                    self.warranty, self.vat, self.net)

class GoodsCategory(models.Model):
    gc_name = models.CharField(max_length=50, default='')
    desc = models.CharField(max_length=200, default='')
    def __str__(self):
        return str(self.id) + " : " + self.gc_name + " : " + self.desc

class Goods(models.Model):
    goodscategory = models.ForeignKey(GoodsCategory, on_delete=models.CASCADE, default=None)
    gid = models.CharField(max_length=13, primary_key=True, default='')
    name = models.CharField(max_length=50, default='')
    brand = models.CharField(max_length=20, default='')
    model1 = models.CharField(max_length=100, default='')
    price = models.FloatField(default=0.00)
    net = models.IntegerField(default=0)
    property = models.TextField(max_length=400, default='')
    def __str__(self):
        return self.gid + " : " + self.name + " : " + self.brand + " : " + self.model1 \
               + " : " + str(self.price) + " : " + str(self.net) + " : " + self.property

class Customer(models.Model):
    cid = models.CharField(max_length=13, primary_key=True, default='')
    name = models.CharField(max_length=30, default='')
    surname = models.CharField(max_length=30, default='')
    address = models.TextField(max_length=200, default="")
    telephone = models.CharField(max_length=10, default='')
    gender = models.BooleanField(default=True)
    career = models.CharField(max_length=30, default='')
    password = models.CharField(max_length=8, default='')

    def __str__(self):
        return self.cid + " : " + self.name + " : " + self.surname

import datetime
class Order(models.Model):
    oid = models.CharField(max_length=13, primary_key=True, default='')
    date = models.DateField(default=datetime.date.today())
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None)
    status = models.CharField(max_length=35, default='')

    def __str__(self):
        return self.oid + " : " + self.status

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default=None)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, default=None)
    price = models.FloatField(default=0.00)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id) + " : " + str(self.price) + " : " + str(self.quantity)
