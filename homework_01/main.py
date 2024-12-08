def open_close_file():
    file = open('data.txt', 'r', encoding='utf-8')
    data = file.readlines()
    file.close()
    return data


# Добавляем в справочник
def add_2_tel(name: str, phone: str, job='unemployee'):
    with open('data.txt', 'a', encoding='utf-8') as one:
        one.write(f'{name};{phone};{job}')

def read_tel():
    with open('data.txt', 'r') as tel:
        data = tel.readlines()
        data = tuple(map(lambda x: x.strip(), data))
        return print(*data, sep='\n')


def save_file():
    with open('data.txt', 'w') as tel:
        tel.write('new_text')

def show_contact():
    with open('data.txt', 'r') as tel:
        data = tel.readlines()
        for cont in data:
            cont_split = cont.split(';')
            return print(f'Name {cont_split[0]}, phone {cont_split[1]}')
        
def create_contact(name, phone, job='unemployee'):
    with open('data.txt', 'a') as tel:
        tel.write(f'{name};{phone};{job};\n')
        print(f'{name};{phone};{job}, created\n')

def find_contact(name):
    with open('data.txt', 'r') as tel:
        for cont in tel:
            cont_split = cont.split(';')
            if cont_split[0] == name:
                print(f'Find Contact. Name {cont_split[0]}, phone {cont_split[1]}')

def change_contact(old_name, new_name):
    with open('data.txt', 'r') as tel:
        lines = tel.readlines()

    with open('data.txt', 'w') as tel:
        for cont in lines:
            if cont.startswith(old_name + ';'):
                new_cont = cont.replace(old_name, new_name, 1)
                print(f'Change Contact. Old name {old_name}, new name {new_name}')
            else:
                 new_cont = cont
            tel.write(new_cont)
            

def remove_contact(name):
    with open('data.txt', 'r') as tel:
        lines = tel.readlines()

    with open('data.txt', 'w') as tel:
        for cont in lines:
            if name not in cont:
                tel.write(cont)
            else:
                print(f'Remove Contact name {name}')


def main():
    # открываем файл
    print('-'*40)
    show_all_cont = open_close_file()
    print('all contact:\n', show_all_cont, '\n')
    print('-'*40)
    read_tel()
    print('-'*40)
    create_contact('Anton', '89992228887', 'just worker')
    print('-'*40)
    find_contact('Anton')
    print('-'*40)
    change_contact('Anton', 'Egor')
    print('-'*40)
    remove_contact('John')


    






if __name__ == '__main__':
    main()