class Perro:
    #Atributos fijos que tienen todos los perros
    patas = 4
    orejas = 2
    ojos = 2

    def __init__(self, raza: str, pelo: str = "Marrón", dueno: str = None):
            # Atributos variables que cambian dependiendo del perro aunque
            # hay opciones por defecto
        self.raza = raza
        self.pelo = pelo
        self.dueno = dueno
        self.velocidad = 0

    def andar(self, aumento_velocidad: float): #Aumentar la velocidad introducida a la que ya tenia
        self.velocidad += aumento_velocidad

    def parar(self): #Para al perro seteando la velocidad a 0
        self.velocidad = 0

    def ladrar(self, texto: str): # Recibe un texto y devuelve el texto con GUAU previamente
        return "GUAU!" + texto


