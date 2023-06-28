from django import forms


class CursoFormulario(forms.Form):

    #Especificar los campos
    curso = forms.CharField()
    codigo = forms.IntegerField()


class NomadesFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=30)