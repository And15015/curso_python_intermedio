def read():
    numbers = []
    with open('./numbers.txt', 'r', encoding = 'utf-8') as f:
        for i in f:
            numbers.append(int(i))
    print(numbers)

def write():
    names =['Karla', 'Migue','Facundo','Rocío']
    with open ('./names.txt', 'w', encoding = 'utf-8') as f:
        for name in names:
            f.write(name)
            f.write('\n')


def run():
    #read()
    write()
    
if __name__ == '__main__':
    run()
    
#     migue
# facundo
# rocio