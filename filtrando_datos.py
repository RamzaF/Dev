from sqlite3 import DatabaseError


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
    # 1.Extrae todo los programadores de Python
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    # 2.Extrae todo los programdores que trabajan en Platzi
    all_Platzi_wokers = [worker["name"] for worker in DATA if worker ["organization"] == "Platzi"]
    # 3. Indica si es mayor a 70 anos en una lista
    old_people = list(map(lambda worker:worker | {"old": worker["age"]>70}, DATA))


    #1
    for worker in all_python_devs:
        print("Desarrollan en Python: " + worker)

    #2
    for worker in all_Platzi_wokers:
        print("Trabajan en Plazi: " + worker)

    #3
    for worker in old_people:
        print(worker)    


if __name__ == '__main__':
    run()