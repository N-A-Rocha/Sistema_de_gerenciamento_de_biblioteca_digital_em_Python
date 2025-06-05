# doc_manager/cli.py
import argparse
from .core import list_documents # Mantemos este import
# from .core import add_document # Adicionaremos este import quando a função existir no core.py

# ... (função handle_list_command permanece a mesma) ...
def handle_list_command(args):
    """
    Lida com o comando 'list'. Chama a função list_documents
    e formata a saída para o console.
    """
    print("\nBuscando documentos na biblioteca...")
    documents_data = list_documents() # Chama a função do core.py

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
                print(f"    - {doc_info['name']}") 
        print("-" * 20) 
    print("\nListagem concluída.")

def handle_add_command(args):
    """
    Lida com o comando 'add'. (Ainda não implementado)
    """
    print(f"\nComando 'add' chamado.")
    print(f"Arquivo a ser adicionado: {args.filepath}")
    print("A lógica para adicionar o arquivo será implementada aqui.")
    # Aqui chamaremos a função core.add_document(args.filepath)

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
    add_parser.set_defaults(func=handle_add_command) # Associa o comando 'add' à sua função manipuladora

    args = parser.parse_args()

    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    run_cli()