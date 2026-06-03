# funcoes.py
from sys import exit # Importação necessária para fechar o programa de forma limpa
from colorama import init, Fore, Style
from database import insert_task, select_task, update_task, delete_task, dash_pendentes_concluidas

init(autoreset=True)

def cad_task():
    titulo = input('Título: ')
    desc = input('Descrição: ')
    prioridade = input('Prioridade: ')
    insert_task(titulo, desc, prioridade)
    print(Fore.GREEN + 'Task cadastrada com sucesso!')

def listar_task():
    tasks = select_task()
    if tasks:

        print(Fore.BLUE + '=' * 40)
        for id_task, titulo, desc, prioridade, status in tasks:
            print(f'ID: {id_task} | Título: {titulo}')
            print(f'Descrição: {desc}')
            print(f'Prioridade: {prioridade} | Status: {status}')
            print(Fore.BLUE + '-' * 40)
    else:
        print(Fore.RED + 'Nenhuma task encontrada!\n')

def atualizar_task():
    listar_task()
    
    try:
        id_task = int(input('Digite o ID da task que deseja atualizar: '))
    except ValueError:
        print(Fore.RED + 'ID inválido! Digite um número.')
        return

    print('\nEscolha o novo status:')
    print('1 - Pendente')
    print('2 - Concluída')
    
    try:
        op = int(input('Digite a opção desejada: '))
    except ValueError:
        print(Fore.RED + 'Opção inválida!')
        return
    
    match op:
        case 1:
            nv_status = 'Pendente'
            update_task(id_task, nv_status)
            print(Fore.GREEN + 'Status atualizado para Pendente com sucesso!')
        case 2:
            nv_status = 'Concluída'
            update_task(id_task, nv_status)
            print(Fore.GREEN + 'Status atualizado para Concluída com sucesso!')
        case _:
            print(Fore.RED + 'Opção inválida! Nenhuma alteração foi feita.')

def excluir_task():
    listar_task()
    
    try:
        id_task = int(input('\nDigite o ID da task que deseja excluir: '))
    except ValueError:
        print(Fore.RED + 'ID inválido! Digite um número.')
        return
        
    delete_task(id_task) 
    print(Fore.GREEN + f'Task com ID {id_task} excluída com sucesso!')

def relatorio():
    r = dash_pendentes_concluidas()
    if r:
        total = sum([n[1] for n in r])
        print(Fore.BLUE + 'Relatório de Tarefas')
        for status, count in r:
            percentual = (count / total) * 100 if total > 0 else 0
            print(f'{status}: {count} ({percentual:.2f}%)')
    else:
        print(Fore.RED + 'Nenhuma task encontrada para gerar o relatório!')

def menu():
    print(Fore.BLUE + '------------------------------------------------------------')
    print(Fore.BLUE + '           ANOTA TASK - GERENCIADOR DE TAREFAS')
    print(Fore.BLUE + '------------------------------------------------------------')
    print('1 - Adicionar tasks')
    print('2 - Listar tasks')
    print('3 - Atualizar tasks')
    print('4 - Excluir tasks')
    print('5 - Relatório (tasks pendentes x andamento)')
    print('6 - Sair')

    try:
        op = int(input('Digite a opção desejada: '))
    except ValueError:
        print(Fore.RED + 'Opção inválida! Digite um número.')
        return

    match op:
        case 1:
            print(15 * '-')
            print(Fore.YELLOW + 'CADASTRAR TAREFA')
            print(15 * '-')
            cad_task()  
        case 2: 
            print(15 * '-')
            print(Fore.YELLOW + 'LISTAR TAREFAS')
            print(15 * '-')
            listar_task()
        case 3:
            print(15 * '-')
            print(Fore.YELLOW + 'ATUALIZAR TAREFA')
            print(15 * '-')
            atualizar_task()
        case 4:
            print(15 * '-')
            print(Fore.YELLOW + 'EXCLUIR TAREFA')
            print(15 * '-')
            excluir_task()
        case 5:
            print(15 * '-')
            print(Fore.YELLOW + 'RELATÓRIO DE TAREFAS')
            print(15 * '-')
            relatorio()
        case 6:
            print(Fore.MAGENTA + 'Encerrando o sistema...')
            exit() 
        case _:
            print(Fore.RED + 'Opção inválida! Digite uma opção válida.')