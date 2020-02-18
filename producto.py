class Producto:
  def __init__(self,referencia,nombre,pvp,descripcion):
    self.referencia=referencia
    self.nombre=nombre
    self.pvp=pvp
    self.descripcion=descripcion
  def __str__(self):
    return """
    Referencia  \t {}
    Nombre \t\t {}
    pvp \t\t {}
    Descripcion \t {} """.format(self.referencia,self.nombre,self.pvp,self.descripcion)

class Adorno(Producto):
  pass
class Alimento(Producto):
  productor=""
  distribuidor=""
  def __str__(self):
    return  super().__str() +"""
    Productor \t {}
    Distribuidor \t {}
    """.format(self.productor,self.distribuidor)


al=Alimento(2034,"Botella de aceite de oliva",5,"250ml")
al.productor="La aceitera"
al.distribuidor="Distribuciones S.A"

print(al)