#Relación entre elementos y electronegatividad
#Relación de elementos y su masa molar 
#Relación de viscosidad y temperatura de un Aceite de motor.

import matplotlib.pyplot as plt

elementos = ['H', 'C', 'N', 'O', 'F', 'Cl', 'Br', 'I', 'S', 'P']
electronegatividad = [2.20, 2.55, 3.04, 3.44, 3.98, 3.16, 2.96, 2.66, 2.58, 2.19]

#GRAFICA DE BARRAS ELECTRONEGATIVIDAD
plt.figure(figsize=(10, 5))
plt.bar(elementos, electronegatividades, color='skyblue')
plt.title('Relación entre Elementos y Electronegatividad')
plt.xlabel('Elementos')
plt.ylabel('Electronegatividad')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

masas_molares = [1.008, 12.011, 14.007, 15.999, 18.998, 35.453, 79.904, 126.90, 32.065, 30.974]

#GRAFICA DE BARRAS MASA MOLAR
plt.figure(figsize=(10, 5))
plt.bar(elementos, masas_molares, color='lightgreen')
plt.title('Relación entre Elementos y Masa Molar')
plt.xlabel('Elementos')
plt.ylabel('Masa Molar (g/mol)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

#VISCOSIDAD Y TEMPERATURA
temperaturas = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180]
viscosidades = [500, 300, 150, 100, 75, 50, 40, 30, 25, 20]  

#GRACIAS LINEAL VISCOSIDAD Y TEMPERATURA

plt.figure(figsize=(10, 5))
plt.plot(temperaturas, viscosidades, marker='o', color='orange', label='Viscosidad vs Temperatura')
plt.title('Relación entre Viscosidad y Temperatura')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Viscosidad (cP)')
plt.grid(linestyle='--', alpha=0.7)
plt.legend()
plt.show()

