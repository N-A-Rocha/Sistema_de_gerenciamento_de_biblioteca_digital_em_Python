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