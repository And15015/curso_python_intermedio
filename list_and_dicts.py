def run():
    my_list = [1, 'Hello' , True , 4.5]
    my_dict = {'first_name': 'Facundo', 'last_name':'Garcia'}

    super_list  = [
        {'first_name': 'Facundo', 'last_name':'Garcia'}, 
        {'first_name': 'Karla', 'last_name':'Orozco'},
        {'first_name': 'Johny', 'last_name':'Vallejo'},
        {'first_name': 'Gloria', 'last_name':'Zapata'},
    ]
    
    super_dict = {
        'nautral_nums': [1,2,3,4,5],
        'integer_nums': [-1,-2,0,1,2],
        'floating_nums': [1.1, 4.5 , 6.43]
    }

    for key, value in super_dict.items():
        print(key, ' - ', value)

    for values in super_list:
        for key,value in values.items():
            print(key, ' - ', value)

if __name__ == '__main__':
    run()