# doc_manager/cli.py
import argparse
from .core import list_documents # Importa a função do nosso módulo core

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
        # Ordena os anos em ordem decrescente para visualização (mais recentes primeiro)
        sorted_years = sorted(years_data.keys(), key=lambda y: (isinstance(y, str), y), reverse=True)

        for year in sorted_years:
            print(f"  Ano: {year if isinstance(year, int) else 'Ano Desconhecido'}")
            if not years_data[year]:
                # Isso não deveria acontecer se a estrutura de dados for sempre preenchida corretamente
                print("    (Nenhum documento para este ano)")
                continue
            for doc_info in years_data[year]:
                print(f"    - {doc_info['name']}") 
                # No futuro, poderíamos adicionar uma opção --verbose para mostrar o caminho completo
                # print(f"      Caminho: {doc_info['path']}") 
        print("-" * 20) # Linha separadora para cada tipo
    print("\nListagem concluída.")


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
    list_parser.set_defaults(func=handle_list_command) # Associa o comando 'list' à sua função manipuladora

    args = parser.parse_args()

    # Chama a função que foi associada ao subcomando (definida em set_defaults)
    if hasattr(args, 'func'):
        args.func(args)
    else:
        # Se por algum motivo 'func' não estiver definida (não deveria acontecer aqui)
        parser.print_help()

if __name__ == '__main__':
    run_cli()