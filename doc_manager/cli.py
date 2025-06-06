# doc_manager/cli.py
import argparse
# Importamos todas as funções que a CLI utiliza
from .core import list_documents, add_document, rename_document, remove_document

# A função handle_list_command permanece a mesma
def handle_list_command(args):
    # ... (código existente sem alterações) ...
    print("\nBuscando documentos na biblioteca...")
    documents_data = list_documents()
    # ... (resto da função)

# A função handle_add_command permanece a mesma
def handle_add_command(args):
    # ... (código existente sem alterações) ...
    print(f"\nAdicionando o arquivo: '{args.filepath}'...")
    sucesso, mensagem = add_document(args.filepath)
    print(mensagem)

# A função handle_rename_command permanece a mesma
def handle_rename_command(args):
    # ... (código existente sem alterações) ...
    print(f"\nRenomeando o arquivo '{args.old_name}' para '{args.new_name}'...")
    sucesso, mensagem = rename_document(args.old_name, args.new_name)
    print(mensagem)


def handle_remove_command(args):
    """
    Lida com o comando 'remove', chamando a função core.remove_document
    e mostrando o resultado para o usuário.
    """
    print(f"\nRemovendo o arquivo: '{args.filename}'...")

    # Chama a função do core.py
    sucesso, mensagem = remove_document(args.filename)

    # Imprime a mensagem retornada pela função (seja de sucesso ou erro)
    print(mensagem)


def run_cli():
    parser = argparse.ArgumentParser(
        description="Sistema de Gerenciamento de Documentos Digitais da Biblioteca",
        prog="doc_manager" 
    )
    parser.add_argument(
        '--version', 
        action='version', 
        version='%(prog)s 0.1.0', 
        help="Mostra a versão do programa e sai."
    )

    subparsers = parser.add_subparsers(dest='command', help='Comandos disponíveis. Digite "comando -h" para ajuda específica.')
    subparsers.required = True 

    # --- Parser para o comando 'list' ---
    list_parser = subparsers.add_parser('list', help='Lista todos os documentos na biblioteca.')
    list_parser.set_defaults(func=handle_list_command)

    # --- Parser para o comando 'add' ---
    add_parser = subparsers.add_parser('add', help='Adiciona um novo documento à biblioteca.')
    add_parser.add_argument('filepath', type=str, help='Caminho completo para o arquivo a ser adicionado.')
    add_parser.set_defaults(func=handle_add_command) 

    # --- Parser para o comando 'rename' ---
    rename_parser = subparsers.add_parser('rename', help='Renomeia um documento existente na biblioteca.')
    rename_parser.add_argument('old_name', type=str, help='Nome do arquivo atual (com extensão).')
    rename_parser.add_argument('new_name', type=str, help='Novo nome para o arquivo (com extensão).')
    rename_parser.set_defaults(func=handle_rename_command)

    # --- Parser para o comando 'remove' ---
    remove_parser = subparsers.add_parser('remove', help='Remove um documento da biblioteca.')
    remove_parser.add_argument('filename', type=str, help='Nome do arquivo a ser removido (com extensão).')
    remove_parser.set_defaults(func=handle_remove_command)

    args = parser.parse_args()

    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    run_cli()