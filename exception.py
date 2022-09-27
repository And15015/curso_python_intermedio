# #USAR TRy con error

# def palindrome(string):
#     return string == string [::-1]

# try:
#     print(palindrome(1))
# except TypeError:
#     print('Solo se pueden ingresar strings')
  
# if __name__ == '__main__':
#     palindrome()


#USAR TRy y RAISE con error
# def palindrome(string):
#     try:
#         if len(string) == 0:
#             raise ValueError('No se puede ingresar cadena vacia')
#         return string == string [::-1]
#     except ValueError as ve:
#         print(ve)
#         return False
  
# if __name__ == '__main__':
#     palindrome()

#USAR FINALLY

try:
    f = open('archivo.txt')
finally:
    f.close()