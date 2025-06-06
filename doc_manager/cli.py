# doc_manager/cli.py
import argparse
from .core import list_documents, add_document, rename_document, remove_document

# MUDANÇA 1: Lógica dentro da função para usar a flag 'verbose'
def handle_list_command(args):
    """
    Lida com o comando 'list'. Chama a função list_documents
    e formata a saída para o console.
    """
    print("\nBuscando documentos na biblioteca...")
    documents_data = list_documents()

    if not documents_data:
        print("Nenhum documento encontrado na biblioteca.")
        return

    print("Documentos encontrados:\n")
    for file_type, years_data in documents_data.items():
        print(f"--- {file_type.upper()} ---")
        sorted_years = sorted(years_data.keys(), key=lambda y: (isinstance(y, str), y), reverse=True)
        
        for year in sorted_years:
            print(f"  Ano: {year if isinstance(year, int) else 'Ano Desconhecido'}")
            if not years_data[year]:
                print("    (Nenhum documento para este ano)")
                continue
            for doc_info in years_data[year]:
                # Lógica condicional baseada na nova flag --verbose
                if args.verbose:
                    print(f"    - {doc_info['name']} (Caminho: {doc_info['path']})")
                else:
                    print(f"    - {doc_info['name']}")
        print("-" * 20)
    print("\nListagem concluída.")


def handle_add_command(args):
    # ... (código existente sem alterações) ...
    print(f"\nAdicionando o arquivo: '{args.filepath}'...")
    sucesso, mensagem = add_document(args.filepath)
    print(mensagem)


def handle_rename_command(args):
    # ... (código existente sem alterações) ...
    print(f"\nRenomeando o arquivo '{args.old_name}' para '{args.new_name}'...")
    sucesso, mensagem = rename_document(args.old_name, args.new_name)
    print(mensagem)


def handle_remove_command(args):
    # ... (código existente sem alterações) ...
    print(f"\nRemovendo o arquivo: '{args.filename}'...")
    sucesso, mensagem = remove_document(args.filename)
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

    # MUDANÇA 2: Adicionando o argumento --verbose ao parser do 'list'
    list_parser = subparsers.add_parser('list', help='Lista todos os documentos na biblioteca.')
    list_parser.add_argument(
        '-v', '--verbose',
        action='store_true', # Isso faz com que ele funcione como uma flag (sem precisar de valor)
        help='Mostra uma listagem detalhada, incluindo o caminho completo dos arquivos.'
    )
    list_parser.set_defaults(func=handle_list_command)

    # ... (código dos outros parsers sem alterações) ...
    add_parser = subparsers.add_parser('add', help='Adiciona um novo documento à biblioteca.')
    add_parser.add_argument('filepath', type=str, help='Caminho completo para o arquivo a ser adicionado.')
    add_parser.set_defaults(func=handle_add_command) 

    rename_parser = subparsers.add_parser('rename', help='Renomeia um documento existente na biblioteca.')
    rename_parser.add_argument('old_name', type=str, help='Nome do arquivo atual (com extensão).')
    rename_parser.add_argument('new_name', type=str, help='Novo nome para o arquivo (com extensão).')
    rename_parser.set_defaults(func=handle_rename_command)

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