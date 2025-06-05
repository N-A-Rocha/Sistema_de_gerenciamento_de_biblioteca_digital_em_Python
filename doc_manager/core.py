import os
import re

# Define o caminho base para a biblioteca de documentos.
# Pode ser ajustado ou vir de uma configuração no futuro.
BASE_LIBRARY_PATH = os.path.join(os.path.dirname(__file__), '..', 'digital_library_files')

def get_file_type_and_year(filename):
    """
    Extrai o tipo de arquivo (extensão) e o ano do nome do arquivo.
    Assume que o ano está no formato _AAAA antes da extensão.
    Retorna "Ano Desconhecido" se o padrão não for encontrado.
    """
    name_part, ext_part = os.path.splitext(filename)
    file_type = ext_part.lower().replace('.', '') # ex: 'pdf', 'epub'

    year = "Ano Desconhecido"
    # Tenta encontrar _AAAA no nome do arquivo (ex: nome_arquivo_2023.pdf)
    match = re.search(r'_(\d{4})', name_part)
    if match:
        year = int(match.group(1))

    return file_type, year

def list_documents(library_path=BASE_LIBRARY_PATH):
    """
    Lista todos os documentos em um dado caminho da biblioteca, 
    organizados por tipo de arquivo e ano de publicação.
    """
    organized_docs = {}

    # os.walk percorre a árvore de diretórios.
    # Para cada diretório, ele produz uma tupla (caminho_dir, nomes_subdirs, nomes_arquivos).
    for dirpath, dirnames, filenames in os.walk(library_path):
        for filename in filenames:
            # Ignora arquivos ocultos (ex: .gitkeep, .DS_Store)
            if filename.startswith('.'):
                continue

            file_type, year = get_file_type_and_year(filename)
            full_path = os.path.join(dirpath, filename)

            # Cria a estrutura do dicionário se as chaves não existirem
            if file_type not in organized_docs:
                organized_docs[file_type] = {}

            if year not in organized_docs[file_type]:
                organized_docs[file_type][year] = []

            organized_docs[file_type][year].append({
                'name': filename,
                'path': full_path
            })

    return organized_docs