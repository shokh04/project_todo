import service
from dto import UserRegisterDTO
from utils import ResponseData
from colorama import Fore


def print_response(response: ResponseData):
    color = Fore.GREEN if response.status else Fore.RED
    print(color + str(response.data) + Fore.RESET)


def print_error(error: Exception):
    print(Fore.RED + str(error) + Fore.RESET)


def menu():
    print('Login    => 1')
    print('Register => 2')
    print('Logout   => 3')
    print('Todo ADD    => 4')
    print('Red todo    => 5')
    print('Delete todo => 6')
    print('Update todo => 7')
    print('Quit     => q')
    return input('?: ')


def authentication():
    username = input('Username: ')
    password = input('Password: ')
    response: ResponseData = service.login(username, password)
    print_response(response)


def register():
    username = input('Username: ')
    password = input('Password: ')
    dto: UserRegisterDTO = UserRegisterDTO(username=username, password=password)
    response: ResponseData = service.register(dto)
    print_response(response)


def logout():
    response: ResponseData = service.logout()
    print_response(response)


def add_todo():
    try:
        title = input('Todo title: ')
        response: ResponseData = service.add_todo(title)
        print_response(response)
    except Exception as e:
        print_error(e)

def read_todo():
    try:
        response: ResponseData = service.read_todo()
        print_response(response)
    except Exception as e:
        print_error(e)


def delete_todos():
    try:
        _id = str((input('Todo id: ')))
        response: ResponseData = service.delete_todo(_id)
        print_response(response)
    except Exception as e:
        print_error(e)


def update_todo():
    try:
        id = str((input('Todo id: ')))
        title = str(input('Todo title: '))
        response: ResponseData = service.update_todo(title, id)
        print_response(response)
    except Exception as e:
        print_error(e)



if __name__ == '__main__':
    while True:
        choice = menu()
        if choice == '1':
            authentication()
        elif choice == '2':
            register()
        elif choice == '3':
            logout()

        elif choice == '4':
            add_todo()
        elif choice == '5':
            read_todo()
        elif choice == '6':
            delete_todos()
        elif choice == '7':
            update_todo()
        elif choice == 'q':
            break
