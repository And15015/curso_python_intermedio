def divisor(num):
    divisor = []
    for i in range(1, num + 1):
        if num % i ==0:
            divisor.append(i)
        return divisor
            
def run():
    
    num = (input('Ingrese un numero:  '))
    assert num.isnumeric(), 'Debes ingresar un numero'
    print(divisor(int(num)))
    print('Terminó el programa')
        
    
if __name__ == '__main__':
     run()