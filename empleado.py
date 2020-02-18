class Persona:
    def __init__(self, cedula, nombre, apellido, direccion):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion

    def __str__(self):
        return """
    Cedula:\t  {}
    Nombre:\t {}
    Apellido:\t {}
    Direccion: \t {}""".format(self.cedula, self.nombre, self.apellido, self.direccion)


class Empleado(Persona):
    def __init__(self, cedula, nombre, apellido, direccion, sueldo, dependencia):
        super().__init__(cedula, nombre, apellido, direccion)
        self.sueldo = sueldo
        self.dependencia = dependencia

    def __str__(self):
        return super().__str__()+"""
    Sueldo: \t {}
    Direccion: \t {}
    """.format(self.sueldo, self.dependencia)


e = Empleado(11205043, "Francisco", "Guedez",
             "Delfin Mendoza", 100000, "Administracion")
print(e)
