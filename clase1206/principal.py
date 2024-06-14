""""

import funciones_matematicas

numero1 = 6
numero2 = 6

resultado = funciones_matematicas.suma(numero1,numero2)
print(f"resultado: {resultado}")

"""

""""
from funciones_matematicas import suma,resta

numero1 = 6
numero2 = 6

resultado = suma(numero1,numero2)
print(f"resultado: {resultado}")
"""

""""
from funciones_matematicas import suma as sm5
from nombre_modulo import suma as sm 


numero1 = 6
numero2 = 6

resultado = sm5(numero1,numero2)
print(f"resultado: {resultado}")
"""

"""
from funciones.funciones_matematicas import suma 

numero1 = 6
numero2 = 6

resultado = suma(numero1,numero2)
print(f"resultado: {resultado}")

"""

from funciones import suma, resta, PI

numero1 = 6
numero2 = 6

resultado = suma(numero1,numero2)
print(f"resultado: {resultado} --- pi= {PI}")
print(f"resultado: {resta(9,8)} --- pi= {PI}")
