
# def run():
#     f = int(input('Ingrese un numero:  '))
    
#     try:
#         assert f >= 0
#         print(f'Muy bien!!, tu numero es ---> {f}')
             
#     except AssertionError:
#         print('Debes ingresar un numero positivo')
    

# if __name__ == '__main__':
#     run()
 
 #---------------------------------

# def run():
#     f = int(input('Ingrese un numero:  '))
    
#     try:
#         assert f >= 0
#         print(f'Muy bien!!, tu numero es ---> {f}')
             
#     except Exception as e:
#         print('Debes ingresar un numero positivo')
#         print((e.__traceback__))
    

# if __name__ == '__main__':
#     run()


 #---------------------------------

def divisor(num):
    divisor = []
    for i in range(1, num + 1):
        if num % i ==0:
            divisor.append(i)
        return divisor
            
def run():
    try:
        
        num = int(input('Ingrese un numero:  '))
        print(divisor(num))
        print('Terminó el programa')
        
    except ValueError:
        print('Debes ingresar un numero')
    
    
if __name__ == '__main__':
     run()
