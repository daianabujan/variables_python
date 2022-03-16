# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia

- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''

print('¡Nuestra primera calculadora!')
# Empezar aquí la resolución del ejercicio

# Tomado como ejemplo y adaptado: https://eiposgrados.com/blog-python/como-hacer-calculadora-python/ 


print('Ingrese por consola el primer número a operar:')
numero_1 = int(input())
 
print('Ingrese por consola el segundo número a operar:')
numero_2 = int(input())
 
opcion=input('Indique la opción deseada: \n\
A a=Suma \n\
B b=Resta \n\
C c=Multiplicación \n\
D d=División \n\
E e=Exponente/Potencia \n\
F f=Modificar los números \n\
G g=Salir'
)

opcion = opcion.lower()

# ACÁ DA ERROR
if opcion == 'a':
print(' ')
print('La suma entre', numero_1, 'y', numero_2, 'es', numero_1+numero_2)
if opcion == 'b':
print(' ')
print('La resta entre', numero_1, 'y', numero_2, 'es', numero_1-numero_2)
if opcion == 'c':
print(' ')
print('La multiplicación entre', numero_1, 'y', numero_2, 'es', numero_1*numero_2)
if opcion == 'd':
print(' ')
print('La división entre', numero_1, 'y', numero_2, 'es', float(numero_1/numero_2))
if opcion == 'e':
print(' ')
print('El exponente entre' , numero_1, 'y', numero_2, 'es', numero_1**numero_2)
if opcion == 'f':
numero_1 = int(input('Ingrese por consola el primer número a operar: ') )
numero_2 = int(input('Ingrese por consola el segundo número a operar: ') )
if opcion == 'g':
print('Chau')
