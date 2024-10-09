# papel = ganar a piedra 
# else:
#     puede perder contra tijera 
#     print(ganaste)


eleccion = input("Piedra papel o tijera: ")
contrincante = input("Piedra papel o tijera: ")

if eleccion == "papel" and contrincante == "piedra" or contrincante == "papel" and eleccion == "piedra":
    print("Gano papel")

if eleccion == "tijera" and contrincante == "piedra"or contrincante == "tijera" and eleccion=="piedra" :
    print("ganò piedra")
    
if eleccion == "tijera" and contrincante== "papel" or contrincante == "tijera" and eleccion== "papel" :
    print("ganò tijera")

if eleccion == contrincante:
    print ("empate por giles")
    
    
