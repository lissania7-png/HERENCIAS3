from clases.herencia1.taxi import Taxi 
from clases.herencia1.auto_particular import AutoParticular
def main(): 
    coche = Taxi("123-GTO","Versa",1000,"123-a") 
    print("********")
    print(coche) 
    coche.encender() 
    coche.subirPasajeros() 
    coche.acelerar() 
    coche.frenar() 
    coche.cobrarCuota() 
    
    ap=AutoParticular("123","Lissania",18,"porsche 911 gt3","negro","G-487")
    print(ap)
    ap.subirseAuto()
    ap.arracarAuto()
    ap.llegarDestino()
    ap.bajandoAuto()
    
if __name__ == '__main__': 
    main()