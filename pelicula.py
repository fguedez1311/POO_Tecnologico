class Pelicula:
  def __init__(self,titulo,duracion,lanzamiento):
    self.titulo=titulo
    self.duracion=duracion
    self.lanzamiento=lanzamiento
  def __str__(self):
    return '{} {}'.format(self.titulo,self.lanzamiento)
class Catalogo:
    peliculas=[]
    def __init__(self,peliculas=[]):
      self.peliculas=peliculas
    def agregar(self,p):
      self.peliculas.append(p)
    def mostrar(self):
      for p in self.peliculas:
        print(p)

p=Pelicula("El padrino 1",175,1972)
c=Catalogo([p])
p1=Pelicula("El padrino 2 ",200,1984)
c.agregar(p1)
c.mostrar()
