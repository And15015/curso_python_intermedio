def run():
    frase = 'las flores son azules'
    e = int(input('Ingrese el indice con el que empieza:  '))
    f = int(input('Ingrese el indice con el que termina:  '))
    for i in range(len(frase)):
        palabra = frase[e:f]
    print(palabra)

if __name__ == '__main__':
    run()