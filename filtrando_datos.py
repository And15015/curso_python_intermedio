DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():
    #Aqui traigo el nombre de los trabajadores cuyo lenguaje de programacion == 'python
    #all_pythoin_devs = [worker['name'] for worker in DATA if worker['language']=='python']
    # for worker in all_pythoin_devs:
    #     print(worker)
    
    #Ahora los trabajadores cuya organizacion == 'Platiz'
    # all_platzi_worker = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi' ]
    # for worker in all_platzi_worker:
    #     print(worker)
    
    #Ahora lo haremos con funciones de orden superior
    #traemos el diccionario completo de las personas > 18 años
    # adults = list(filter(lambda worker: worker['age'] > 18, DATA))
    # #Ahora traeremos solo namore y edad
    # adutls = list(map(lambda worker:worker['name'],adults))
    # for worker in adults:
    #     print(worker)
    
    #Ahora le vamos a añadir otro parametro al diccionario con el comando pipe |
    # old_people = list(map(lambda worker:worker | {'old':worker['age'] > 70},DATA))
    # for worker in old_people:
    #      print(worker)
    
    
    #Ahora creare listas usando filter y map COMBINADOS
    # all_python_devs2 = list(map(lambda worker:worker['name'], list(filter(lambda worker:worker['age'] > 18,DATA))))
    # for worker in all_python_devs2:
    #     print(worker)
        
        
    #USAR LISTAS COMPRENSIVAS CON ADULOTS Y ALL_PEOPLE
    
    # adult2 = [worker['name'] for worker in DATA if worker['age'] > 18]
    # print(adult2)
    
    old_people2 = [i | {'old':i['age'] > 70 } for i in DATA]
    print(old_people2)
    
if __name__ == '__main__':
    run()
    
    