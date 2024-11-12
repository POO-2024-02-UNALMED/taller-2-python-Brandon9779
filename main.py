class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, nuevo_color):
        if nuevo_color in ["rojo", "verde", "amarillo", "negro", "blanco"]:
            self.color = nuevo_color


class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, nuevo_registro):
        self.registro = nuevo_registro

    def asignarTipo(self, nuevo_tipo):
        if nuevo_tipo in ["electrico", "gasolina"]:
            self.tipo = nuevo_tipo


class Auto:
    cantidadCreados = 0

    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.marca = marca
        self.asientos = asientos
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        cantidad = 0
        for asiento in self.asientos:
            if asiento is not None:
                cantidad += 1
        return cantidad

    def verificarIntegridad(self):
        if self.registro != self.motor.registro:
            return "Las piezas no son originales"
        
        for asiento in self.asientos:
            if asiento is not None and asiento.registro != self.registro:
                return "Las piezas no son originales"
        
        return "Auto original"

    @staticmethod
    def incrementarCantidadCreados():
        Auto.cantidadCreados += 1

    @staticmethod
    def obtenerCantidadCreados():
        return Auto.cantidadCreados
