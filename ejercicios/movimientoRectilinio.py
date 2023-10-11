print("Calcular distancias MRU (m/s) :\n ")
 

#Velocidad es v = d/t
#distancia es d = v * t

v = float(input("Ingrese su velocidad :"))
t = float(input("Ingrese el tiempo : \n"))
 
 
distancia = (v * 1000) * (t/3600)

print(f"La distancia recorrida es :{ distancia }") 

 