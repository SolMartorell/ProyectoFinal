from django.forms import Form, CharField, IntegerField, EmailField, BooleanField


class ActividadesFormulario(Form):
    nombre = CharField(max_length=30)
    dia = CharField(max_length=30)
    horario = IntegerField()
    cupo = IntegerField()

class SociosFormulario(Form):
    nombre = CharField(max_length=30)
    apellido = CharField(max_length=30)
    email = EmailField()
    cuota_paga = BooleanField()

class PlanesFormulario(Form):
    nombre = CharField(max_length=30)
    cantidad_clases = IntegerField()
    precio = IntegerField()