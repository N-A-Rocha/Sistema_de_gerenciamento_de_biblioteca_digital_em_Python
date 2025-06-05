# doc_manager/cli.py
import argparse
# A função list_documents será importada quando precisarmos dela.
# from .core import list_documents 

def run_cli():
    parser = argparse.ArgumentParser(
        description="Sistema de Gerenciamento de Documentos Digitais da Biblioteca",
        prog="doc_manager" # Define o nome do programa que aparecerá na ajuda
    )
    parser.add_argument(
        '--version', 
        action='version', 
        version='%(prog)s 0.1.0', # Uma forma de adicionar a versão
        help="Mostra a versão do programa e sai."
    )

    subparsers = parser.add_subparsers(dest='command', help='Comandos disponíveis. Digite "comando -h" para ajuda específica.')
    subparsers.required = True # Torna um subcomando obrigatório

    # --- Parser para o comando 'list' (ainda sem a funcionalidade completa) ---
    list_parser = subparsers.add_parser('list', help='Lista todos os documentos na biblioteca.')
    # No futuro, aqui poderíamos adicionar argumentos específicos para o 'list', como --type ou --year
    # list_parser.set_defaults(func=handle_list_command) # Preparando para uma função que lidará com o comando

    args = parser.parse_args()

    # Por enquanto, vamos apenas verificar se o comando 'list' é reconhecido
    if args.command == 'list':
        print("Comando 'list' chamado. A lógica de listagem será implementada aqui.")
        # Aqui chamaremos a função que realmente lista os documentos.
        # Ex: handle_list_command(args)
    else:
        # Se um comando desconhecido for passado (não deveria acontecer com subparsers.required=True)
        # ou se a lógica de despacho de comandos ficasse mais complexa.
        print(f"Comando '{args.command}' não implementado ou desconhecido.")
        parser.print_help()

if __name__ == '__main__':
    run_cli()