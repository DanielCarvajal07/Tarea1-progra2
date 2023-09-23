# Ejercicio 4
# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.


list=[]
for i in range(6):
  list.append(int(input('Ingrese número ganador: ')))
list.sort()
print('Números ganadores: ')
print(*list, sep=', ')
print(f'Números ganadores: {", ".join(str(x) for x in list)}')
print('Números ganadores: {} {} {} {} {} {}'.format(*list))