from time import sleep
from services.storage import carregar_dados, salvar_dados

def adicionar_tarefa():

    """Pede ao usuário para digitar o título da tarefa, cria um dicionário com o título e o status de conclusão, carrega os dados existentes, adiciona a nova tarefa à lista de tarefas, salva os dados atualizados e exibe mensagens de confirmação."""

    titulo = input('Digite a tarefa que deseja adicionar: ')

    tarefa = {
        'titulo' : titulo,
        'concluida' : False
    }

    dados_conteudo = carregar_dados()

    dados_conteudo.append(tarefa)

    salvar_dados(dados_conteudo)

    print('Adicionando tarefa...')
    sleep(1)

    print(f'Tarefa "{titulo}" adicionada com sucesso!')
    sleep(1)

def excluir_tarefa():

    """Pede ao usuário para digitar o número da tarefa que deseja excluir, carrega os dados existentes, verifica se a tarefa existe, remove a tarefa da lista de tarefas, salva os dados atualizados e exibe mensagens de confirmação."""
    
    dados_conteudo = carregar_dados()

    if not dados_conteudo:

        print('Nenhuma tarefa encontrada para excluir.')

    else:

        listar_tarefas()

        num_tarefa_concluida = ' '
        
        while num_tarefa_concluida not in range(1, len(dados_conteudo) + 1):

            num_tarefa_concluida = int(input('Digite o número da tarefa que deseja excluir: '))

            if num_tarefa_concluida not in range(1, len(dados_conteudo) + 1):

                print('Não existe tarefa com esse número. Tente novamente.')

            else:
                
                dados_conteudo.remove(dados_conteudo[num_tarefa_concluida-1])

                print('Excluindo tarefa...')
                sleep(1)

                print(f'Tarefa {dados_conteudo[(num_tarefa_concluida - 1)].get("titulo")} excluída com sucesso!')
    sleep(1)
    
    salvar_dados(dados_conteudo)

def listar_tarefas():

    """Lista todas as tarefas existentes no arquivo JSON."""

    dados_conteudo = carregar_dados()

    print('=' * 50)
    
    if not dados_conteudo:
        
        print('Nenhuma tarefa encontrada.')

    else:

        print(' Tarefas:')
        sleep(0.5)

        for ind, tarefa in enumerate(dados_conteudo):

            status = 'Concluída' if tarefa.get('concluida') else 'Pendente'

            print(f' {ind + 1} - {tarefa.get("titulo")} - {status}')
            sleep(0.5)

    sleep(0.5)

def marcar_tarefa():

    """Pede ao usuário para digitar o número da tarefa que deseja marcar como concluída ou pendente, carrega os dados existentes, verifica se a tarefa existe, alterna o status de conclusão da tarefa, salva os dados atualizados e exibe mensagens de confirmação."""

    dados_conteudo = carregar_dados()

    if not dados_conteudo:

        print('Nenhuma tarefa encontrada.')

    else:

        listar_tarefas()

        num_tarefa_concluida = ' '
        
        while num_tarefa_concluida not in range(1, len(dados_conteudo) + 1):

            num_tarefa_concluida = int(input('Digite o número da tarefa que deseja marcar como concluída: '))

            if num_tarefa_concluida not in range(1, len(dados_conteudo) + 1):

                print('Não existe tarefa com esse número. Tente novamente.')

            else:

                tarefa = dados_conteudo[num_tarefa_concluida - 1]
                tarefa['concluida'] = True if not tarefa['concluida'] else False
                dados_conteudo[num_tarefa_concluida - 1] = tarefa

                salvar_dados(dados_conteudo)

                status = 'Concluída' if tarefa['concluida'] else 'Pendente'

                print(f'Marcando tarefa "{tarefa.get("titulo")}" como {status}...')
                sleep(1)

                print(f'Tarefa "{tarefa.get("titulo")}" marcada como {status} com sucesso!')

    sleep(1)