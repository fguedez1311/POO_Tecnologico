class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def visualizar(self):
        return '''
        Nombre \t {}
        Edad \t {}'''.format(self.nombre, self.edad)


class Estudiante(Persona):
    def __init__(self, nombre, edad, id):
        super().__init__(nombre, edad)
        self.id = id

    def visualizar(self):
        return super().visualizar()+"\n"+"\t id\t{}" .format(self.id)


class Profesor(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario = salario

    def visualizar(self):
        return super().visualizar()+"\n"+"\t id\t{}" .format(self.salario)

print("Datos de persona")
p = Persona("Francisco", 18)
print(p.visualizar())

print("Datos de Estudiante")
e = Estudiante("Francisco", 18, 4879)
print(e.visualizar())

print("Datos del profesor")
pr = Profesor("Angel", 32, 4500)
print(pr.visualizar())
