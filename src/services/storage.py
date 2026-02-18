import json
from time import sleep

arquivo_tarefas = 'data/data.json'

def carregar_dados():

    """Carrega os dados_conteudo do arquivo_tarefas JSON. Se o arquivo não existir ou estiver vazio, retorna uma lista vazia."""
    
    try:
        with open(arquivo_tarefas, 'r') as arq:

            dados_conteudo = json.load(arq)

            return dados_conteudo
        
    except (FileNotFoundError, json.JSONDecodeError):

        return []
    
def salvar_dados(dados_salvar):

    """Salva os dados_conteudo no arquivo_tarefas JSON. Se o arquivo não existir, ele será criado."""
    
    print('Salvando dados...')

    with open(arquivo_tarefas, 'w') as arq:

        json.dump(dados_salvar, arq, indent=4)
        
        sleep(1)
        print('Dados salvos com sucesso!')