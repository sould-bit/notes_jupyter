
# # MODULOS
#  es un archivo con la etencion de un lenguaje 

import sys 
print(sys.path)

# # expreciones regulares 

import re

text = 'this tex is an example 311 394 3902 con codigo 57 '


exprecion_regular = re.findall('[0-9]+', text)
print(exprecion_regular)


import time 
timestamp = time.time()
local = time.localtime()
result = time.asctime(local)
print(timestamp)
print(local)
print(result)

import collections

numbers =[1,1,1,1,2,2,3,3,34,4,55,6,6,77,2,2,2,2,2,3,4]

count = collections.Counter(numbers)

print(count)


    # - podemos hacer nuestros propios modulos he importar sus funciones 
import fil


dato = [
    {

            'city' : 'colombia',
            'population': '300'
        
        },
        {
            'city': 'brazil',
            'population': '400'
        }
    ]

user = input('type city')
    # archivo .funcion a importar (parametros)
all = fil.func(dato, user)
print(all)




# %%