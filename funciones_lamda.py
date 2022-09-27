#lambda argumentos:expresion
#en lugar de def vamos a usar lambda
# palindrome = lambda string: string == string[::-1]
# print(palindrome('ana'))

#asi se haria con funciones normales

# def palindrome(string):
#     return string == string[::-1]
# print(palindrome('ana'))

#LISTA DE ORDEN SUPERIOR CON FUNCION 'MAP'
# my_list = [1,2,3,4,5]
# squares = list(map(lambda x: x**2, my_list))
# print(squares) 


#LISTA DE ORDEN SUPERIOR CON FUNCION 'REDUCE'
from functools import reduce
my_list = [2,2,2,2,2]
all_multiplied = reduce(lambda a,b : a*b, my_list)
print(all_multiplied)
