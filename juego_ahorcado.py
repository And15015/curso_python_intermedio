from random import randint


def read_names() -> list:
    with open('./names.txt', 'r') as f:
        words = f.readlines()
    return words  
        

def run(words: list) -> None:
    word = words[randint(0, len(words)-1)].strip()
    
    word_list = list(word)
    
    guiones = '_'*len(word)
    
    guiones_list = list(guiones)
    
    for _ in range(len(word_list)+3):
        letra = input('Ingrese una letra: ')
        letra = letra.lower()
        while True:
            if letra in word_list:
                #print('La letra es correcta')
                idx_word = word_list.index(letra)
                guiones_list[idx_word] = letra
                word_list[idx_word] = '_'  
            else:
                #print('Letra incorrecta')
                break
        print(' '.join(guiones_list))
        if '_' not in guiones_list:
            break
        
    if '_' in guiones_list:
        print('Perdiste')
    else:
        print('Ganaste')





if __name__ == '__main__':
    words = read_names()
    run(words)