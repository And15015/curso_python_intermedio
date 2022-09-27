
def write_names():
    lista_last = list()
    for i in range(0,5):
        solicitud = input('Ingrese apellidos:  ')
        solicitud = solicitud.capitalize()
        lista_last.append(solicitud)
        try: 
            with open('./lastname.txt', 'w') as last:
            
                for i in lista_last:
                    last.write(i)
                    last.write('\n')  
        except:
            print(lista_last)

def run():
    write_names()
     
        
if __name__ == '__main__':
    run()
        