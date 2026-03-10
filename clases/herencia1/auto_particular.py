from clases.herencia2.personas import Persona

class AutoParticular(Persona):
    def __init__(self, clave, nombre, edad,marca,color,placa):
        super().__init__(clave,nombre,edad)
        self.marca = marca
        self.color = color 
        self.placa = placa 
        
    def __str__(self):
        return super().__str__()+" "+ self.marca+" "+self.color+" "+self.placa
        
    def subirseAuto(self):
        print("subiendo al auto")
        
    def  arracarAuto(self):
        print("Encendiendo el radio")
        print("Arrancamdo el auto")
        
    def llegarDestino(self):
        print("Llegando al destino")
    
    def bajandoAuto(self):
        print("Bajando del auto")
    
    
    