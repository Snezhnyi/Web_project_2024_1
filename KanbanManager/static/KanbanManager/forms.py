from django import forms
from django.forms.widgets import Textarea

class cardForm(forms.Form):
    name = forms.CharField(label="Имя", max_length=30)
    description = forms.CharField(label="Описание", widget=Textarea, required=False)
    pilot = forms.CharField(label="Тема", max_length=64)
    estimated = forms.IntegerField(required=False, label="Время выполнения") # in hours
    attached = forms.CharField(label="Ссылка на приложенные файлы", max_length=300, required=False) 
    card_type = forms.CharField(label="Тип карты", max_length=30, required=False)