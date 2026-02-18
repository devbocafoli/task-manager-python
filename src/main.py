from services.storage import *
from services.tarefas import *
from time import sleep

tarefas = []

while True:

    print('=' * 50)

    print('{:^50}'.format('GERENCIADOR DE TAREFAS'))

    print('=' * 50)

    print('  1 - Adicionar Tarefa')
    print('  2 - Excluir Tarefa')
    print('  3 - Listar Tarefas')
    print('  4 - Marcar Tarefa como Concluída/Pendente')
    print('  5 - Sair do Programa')

    print('=' * 50)

    opcao = ' '

    while opcao not in ['1', '2', '3', '4', '5']:

        opcao = input('Digite a Opção Desejada: ')

        if opcao not in ['1', '2', '3', '4', '5']:

            print('Opção Inválida. Tente Novamente.')

        if opcao == '1':

            adicionar_tarefa()

        elif opcao == '2':

            excluir_tarefa()

        elif opcao == '3':

            listar_tarefas()

        elif opcao == '4':

            marcar_tarefa()

        elif opcao == '5':

            print('Saindo do Programa...')
            sleep(2)

            print('Programa Encerrado.')
            break

    if opcao == '5':
        break

