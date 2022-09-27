import math 

def run():
    #my_dict = {}
    
 #  ejemplo 1
 # muestre naturales del 1 al 100 en key
 # y en valor que sea el numero natura al cubo   
    # for i in range(1,1001):
    #     my_dict[i] = (i**3)   
    # print(my_dict)
    
# ejemplo 2
#muestre en la llave los naturales del 1 al 100
#considerando que no sean multiplos de 3
#y en el valor el numero de la llave al cubo
    # for i in range(1,101):
    #     if i % 3 != 0:
    #         my_dict[i] = (i**3)
            
    # print(my_dict)
    
#ejemplo 3
# es el ejemplo anterior en lista comprensiva para diccioario

    # dict_compr = {i:i**3 for i in range(1,101) if i % 3 != 0} 
    # print(dict_compr)

#Reto:
#crear un diccionario 1000 primeros nuemros como llave
#su valor seran las raices cuadradas
# 
    reto = {i:math.sqrt(i) for i in range(1,100)}
    print(reto)



if __name__ == '__main__':
    run()