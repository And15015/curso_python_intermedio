def run():
    squares = []
    
     
        
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         squares.append(i**2)
        
        
    # print('squares', squares)


task = [ i for i in range(1,100) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]

print(task)

# a continuación se presenta una estructura de lista de compresion 

# [element for element in iterable if condition]

# [i**2 for i  in range(1,101) if i % 3 != 0]

if __name__ == '__main__':
    run()