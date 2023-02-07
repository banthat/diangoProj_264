from django import forms

class ProductForm(forms.Form):
    BRAND_LIST = [('Louis Vuitton', 'Louis Vuitton'),
                  ('Hermes', 'Hermes'),
                  ('Chanel', 'Chanel'),
                  ('Dior', 'Dior'),
                  ('Gucci', 'Gucci'),
                  ]

    COLOR_LIST = [('White', 'White'),
                  ('Black', 'Black'),
                  ('Gray', 'Gray'),
                  ('Brown', 'Brown'),
                  ('Cream', 'Cream'),
                  ('Silver', 'Silver'),
                  ('Indigo', 'Indigo'),
                  ('Old Rose', 'Old Rose'),
                  ]

    TYPE_LIST = [('Clutch', 'Clutch'),
                 ('Hobo', 'Hobo'),
                 ('Saddle Bag', 'Saddle Bag'),
                 ('Baguette', 'Baguette'),
                 ('Bowling Bag', 'Bowling Bag'),
                 ('Duffle', 'Duffle'),
                 ('Tote', 'Tote'),
                 ]

    id = forms.CharField(max_length=13, label="รหัสสินค้า",
                         required=True, widget=forms.TextInput(attrs={'size': '15'}))

    brand = forms.CharField(max_length=30, label="ชื่อแบรนด์",  required=True, widget=forms.Select(choices=BRAND_LIST))

    model = forms.CharField(max_length=30, label="ชื่อรุ่น", required=True, widget=forms.TextInput(attrs={'size': '35'}))

    color = forms.CharField(max_length=30, label="สี", required=True, widget=forms.RadioSelect(choices=COLOR_LIST))

    type = forms.CharField(max_length=30, label="ประเภท", required=True, widget=forms.Select(choices=TYPE_LIST))

    price = forms.IntegerField(label="ราคา", required=True, widget=forms.NumberInput(
        attrs={'size': '35', 'min': '2000', 'max': '1000000'}))

from .models import *

class GoodsForm(forms.ModelForm):
    class Meta:
        model = Goods
        fields = ('goodscategory', 'gid', 'name', 'brand', 'model1', 'price', 'net', 'property')
        widgets = {
            'goodscategory': forms.Select(attrs={'class': 'form-control'}),
            'gid': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'model1': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'min': 10, 'max': 100000}),
            'net': forms.NumberInput(attrs={'class': 'form-control'}),
            'property': forms.TextInput(attrs={'class': 'form-control'})
        }
        labels = {
            'goodscategory': 'ประเภท',
            'gid': 'รหัสสินค้า',
            'name': 'ชื่อสินค้า',
            'brand': 'ยี่ห้อ',
            'model1': 'รุ่น',
            'price': 'ราคา',
            'net': 'จำนวน',
            'property': 'คุณสมบัติ',
        }

    def updateForm(self):
        self.fields['gid'].widget.attrs['readonly'] = True
        self.fields['gid'].label = 'รหัสสินค้า [ไม่อนุญาตให้แก้ไขได้]'

    def deleteForm(self):
        self.fields['goodscategory'].widget.attrs['readonly'] = True
        self.fields['gid'].widget.attrs['readonly'] = True
        self.fields['name'].widget.attrs['readonly'] = True
        self.fields['brand'].widget.attrs['readonly'] = True
        self.fields['model1'].widget.attrs['readonly'] = True
        self.fields['price'].widget.attrs['readonly'] = True
        self.fields['net'].widget.attrs['readonly'] = True
        self.fields['property'].widget.attrs['readonly'] = True
