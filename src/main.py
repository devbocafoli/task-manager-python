from services.tarefas import add_task, delete_task, list_tasks, toggle_task_status
from time import sleep

def show_tasks(tasks):

    print(' Tasks:')

    sleep(0.5)

    for idx, task in enumerate(tasks):

        status = 'Completed' if task.get('completed') else 'Pending'

        print(f' {idx + 1} - {task.get("title")} - {status}')

        sleep(0.5)
        

def show_menu():
        
    """Show the main menu of the program."""

    print('=' * 50)

    print('{:^50}'.format('TASK MANAGER'))

    print('=' * 50)

    print('  1 - Add Task')
    print('  2 - Delete Task')
    print('  3 - List Tasks')
    print('  4 - Mark Task as Completed/Pending')
    print('  0 - Exit Program')

    print('=' * 50)

    option = ' '

    while option not in ['1', '2', '3', '4', '0']:

        option = input('Enter the Desired Option: ')

        if option not in ['1', '2', '3', '4', '0']:

            print('Invalid Option. Please Try Again.')

    return option
    

while True:

    option = show_menu()

    if option == '1':

        try:
            task_title = input('Enter the task title: ')
            added_task = add_task(task_title)

            sleep(1)

            print(f'Task {added_task["title"]} added successfully!')

        except ValueError as error:
            print(f'Error: {error}. Please Try Again.')


    elif option == '2':
        
        tasks = list_tasks()

        if not tasks:
            print('No tasks found to delete.')
        else:
            show_tasks(tasks)

        try:
            idx_removed_task = int(input('Enter the index of the task you want to delete: '))
            removed_task = delete_task(idx_removed_task)

            sleep(1)

            print(f'Task "{removed_task.get("title")}" deleted successfully!')

        except ValueError as error:
            print(f'Error: {error}. Please Try Again.')

        except IndexError as error:
            print(f'Error: {error}. Please Try Again.')


    elif option == '3':

        show_tasks(list_tasks())


    elif option == '4':

        tasks = list_tasks()

        if not tasks:
            print('No tasks found to toggle.')
        else:
            show_tasks(tasks)

        try:
            idx_toggle_task = int(input('Enter the index of the task you want to toggle: '))
            toggled_task = toggle_task_status(idx_toggle_task)
            status = 'Completed' if toggled_task.get('completed') else 'Pending'

            sleep(1)

            print(f'Task "{toggled_task.get("title")}" marked as {status}, successfully!')
        
        except ValueError as error:
            print(f'Error: {error}. Please Try Again.')

        except IndexError as error:
            print(f'Error: {error}. Please Try Again.')


    elif option == '0':

        print('Leaving the Program...')
        
        sleep(2)

        print('Program Closed.')
        break

    sleep(1)
