class Tienda:
        #Atributos fijos que tienen todas las tiendas

    tipo = "Electrodomésticos"
    abierta = True

    def __init__(self, nombre: str, direcc: str, numEmp: int, ventas: dict):
        # Atributos variables que cambian dependiendo de la tienda 
        self.nombre = nombre
        self.direcc = direcc
        self.numEmp = numEmp
        self.ventas = ventas

    def calcularVentas(self):   # Recorre todos los empleados que hay y suma todas las ventas que ha tenido cada uno 
                                # En los últimos 3 meses que es todo lo que guarda el array
        total = 0
        for meses in self.ventas.values():
            total += sum(meses)
        return total
 
    def ventasEmpleado(self, empleado: str):  #La media de las ventas que haya tenido cada empleado los últimos 3 meses
         return sum(self.ventas[empleado]) / 3
 
    def datos(self): #Devuelve el nombre y la dirección de la tienda que recibe
        return f"{self.nombre} - {self.direcc}"
 
    def ultimoVenta(self): #Devuelve la última venta de cada mes recorriendo 
                            # y sumando el último mes contando a todos los empleados
        total = 0
        for meses in self.ventas.values():
            total += meses[-1]
        return total
 
    def proyeccion(self, marketing: float): #Multiplica por lo que sea dependiendo de lo que introduzcas
        factor = 1.2 if marketing < 1000 else 1.5
        for emp in self.ventas:
            self.ventas[emp] = [v * factor for v in self.ventas[emp]]
        return self.ventas
 
