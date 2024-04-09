from django import forms
from . models import Customer,item

class addform(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','address','image']
        
        
class updateform(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','address','image']
        
class itemaddform(forms.ModelForm):
    class Meta:
        model = item
        fields = ['name','description','price','image']
        
class itemupdateform(forms.ModelForm):
    class Meta:
        model = item
        fields = ['name','description','price','image']
        
        