class Vehiculo:
  def __init__(self,color,ruedas):
    self.color=color
    self.ruedas=ruedas
  def __str__(self):
    return "Color: \t {}  Ruedas: \t {} ".format(self.color,self.ruedas)

class Coche(Vehiculo):
  def  __init__(self,color,ruedas,velocidad,cilindrada):
    super().__init__(color,ruedas)
    self.velocidad=velocidad
    self.cilindrada=cilindrada
  def __str__(self):
    return  super().__str__()+ ", {}  km/h  {} cc".format(self.velocidad,self.cilindrada)

c=Coche("Azul",4,150,1200)
print(c)
