from readchar import readkey
from sys import exit

CLEAR = chr(27) + '[2J'  # http://stackoverflow.com/a/2084521/1928484
RESET = '\x1b[0m'
SELECTED = '\x1b[30m\x1b[47m'

selected_todo = 0
todos = []


def add_todo():
    todo = input('Add Todo: ')
    todos.append({'done': False, 'title': todo})


def cleanup():
    global todos
    todos = list(filter(lambda todo: not todo['done'], todos))


def render():
    print(CLEAR + RESET, end='')

    if len(todos) is 0:
        print(RESET + 'No Todos!')
    else:
        for i, todo in enumerate(todos):
            print('{}[{}] {}{}'.format(
                SELECTED if i is selected_todo else RESET,
                'X' if todo['done'] else ' ',
                todo['title'],
                RESET
            ))


while True:
    render()
    key = readkey()
    if key == 'q' or key == '\x03':
        exit(0)
    elif key == '\x1b[A':
        if selected_todo is 0:
            continue
        else:
            selected_todo -= 1
    elif key == '\x1b[B':
        if selected_todo is len(todos) - 1:
            continue
        else:
            selected_todo += 1
    elif key == ' ':  # Space just finishes a todo
        todos[selected_todo]['done'] = not todos[selected_todo]['done']
    elif key == '\r' or key == '\n':  # Enter finishes a todo and cleans up
        todos[selected_todo]['done'] = not todos[selected_todo]['done']
        cleanup()
    elif key == 'a':
        add_todo()
    elif key == 'c':
        cleanup()
    elif key == '\x7f' or key == 'd':
        del todos[selected_todo]
