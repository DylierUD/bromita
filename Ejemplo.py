import random

eleccion = input("Piedra papel o tijera: ")
contrincante = random.randint(1,3)

if contrincante == 1:
    contrincante = "papel"
elif contrincante== 2:
     contrincante= "piedra"
else:
    contrincante= "tijera"
      
print(eleccion,"vs", contrincante)

if eleccion == "papel" and contrincante == "piedra" or contrincante == "papel" and eleccion == "piedra":
    print("Gano papel")

if eleccion == "tijera" and contrincante == "piedra"or contrincante == "tijera" and eleccion=="piedra" :
    print("ganò piedra")
    
if eleccion == "tijera" and contrincante== "papel" or contrincante == "tijera" and eleccion== "papel" :
    print("ganò tijera")

if eleccion == contrincante:
    print ("empate por giles")
    
    
