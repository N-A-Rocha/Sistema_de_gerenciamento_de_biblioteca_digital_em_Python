import os
import re
import shutil # Novo import para operações de arquivo (copiar)

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

def add_document(source_filepath, library_path=BASE_LIBRARY_PATH):
    """
    Adiciona um documento à biblioteca, organizando-o em subpastas
    por tipo de arquivo (em maiúsculas) e ano.

    Args:
        source_filepath (str): O caminho completo para o arquivo de origem.
        library_path (str): O caminho base para o diretório da biblioteca.

    Returns:
        tuple: (bool, str) indicando sucesso/falha e uma mensagem descritiva.
    """
    if not os.path.isfile(source_filepath):
        return False, f"Erro: Arquivo de origem não encontrado em '{source_filepath}'."

    filename = os.path.basename(source_filepath)

    # Reutiliza a função existente para obter tipo e ano
    file_type, year = get_file_type_and_year(filename) 

    if not file_type: # Se não houver extensão, não podemos determinar o tipo principal
        file_type_for_path = "SemExtensao" # Pasta para arquivos sem extensão
    else:
        file_type_for_path = file_type.upper() # Ex: PDF, EPUB

    year_for_path = str(year) # Converte o ano para string para usar no caminho

    # Constrói o caminho do diretório de destino
    # Ex: .../digital_library_files/PDF/2023/
    destination_dir = os.path.join(library_path, file_type_for_path, year_for_path)

    try:
        # Cria os diretórios de destino se eles não existirem
        # exist_ok=True evita erro se o diretório já existir
        os.makedirs(destination_dir, exist_ok=True) 
    except OSError as e:
        return False, f"Erro ao criar diretório de destino '{destination_dir}': {e}"

    destination_filepath = os.path.join(destination_dir, filename)

    # Verifica se o arquivo já existe no destino para evitar sobrescrever
    if os.path.exists(destination_filepath):
        return False, f"Erro: O arquivo '{filename}' já existe em '{destination_dir}'."

    # Copia o arquivo para o diretório de destino
    try:
        shutil.copy2(source_filepath, destination_filepath) # copy2 tenta preservar metadados
        return True, f"Documento '{filename}' adicionado com sucesso em '{destination_dir}'."
    except IOError as e: # Erros de entrada/saída, como permissão negada
        return False, f"Erro de E/S ao copiar o arquivo '{filename}': {e}"
    except Exception as e: # Captura outros erros inesperados durante a cópia
        return False, f"Erro inesperado ao adicionar o arquivo '{filename}': {e}"

def rename_document(old_name, new_name, library_path=BASE_LIBRARY_PATH):
    """
    Renomeia um documento na biblioteca e o move para a pasta correta
    se o novo nome implicar uma mudança de tipo ou ano.

    Args:
        old_name (str): O nome de arquivo atual do documento (com extensão).
        new_name (str): O novo nome de arquivo para o documento (com extensão).
        library_path (str): O caminho base para o diretório da biblioteca.

    Returns:
        tuple: (bool, str) indicando sucesso/falha e uma mensagem descritiva.
    """
    source_filepath = None
    found_paths = []

    # 1. Encontrar o caminho completo do arquivo antigo
    for dirpath, dirnames, filenames in os.walk(library_path):
        if old_name in filenames:
            found_paths.append(os.path.join(dirpath, old_name))

    # 2. Lidar com casos de arquivo não encontrado ou duplicado
    if not found_paths:
        return False, f"Erro: Arquivo '{old_name}' não encontrado na biblioteca."
    if len(found_paths) > 1:
        return False, f"Erro: Múltiplos arquivos com o nome '{old_name}' encontrados. Operação ambígua."

    source_filepath = found_paths[0]

    # 3. Determinar o novo caminho com base no novo nome
    new_file_type, new_year = get_file_type_and_year(new_name)

    if not new_file_type:
        new_file_type_for_path = "SemExtensao"
    else:
        new_file_type_for_path = new_file_type.upper()

    new_year_for_path = str(new_year)

    destination_dir = os.path.join(library_path, new_file_type_for_path, new_year_for_path)
    destination_filepath = os.path.join(destination_dir, new_name)

    # 4. Verificar se o novo nome já existe no destino
    if os.path.exists(destination_filepath):
        # Se o caminho de origem e destino for o mesmo, é o mesmo arquivo, não faz sentido renomear para o mesmo nome.
        if source_filepath == destination_filepath:
             return False, f"Erro: O novo nome é idêntico ao nome antigo."
        return False, f"Erro: Um arquivo com o nome '{new_name}' já existe no local de destino."

    # 5. Criar diretório de destino e mover/renomear o arquivo
    try:
        os.makedirs(destination_dir, exist_ok=True)
        shutil.move(source_filepath, destination_filepath) # shutil.move lida com renomear e mover
        return True, f"Arquivo '{old_name}' renomeado para '{new_name}' e movido para '{destination_dir}'."
    except Exception as e:
        return False, f"Erro inesperado ao renomear o arquivo: {e}"


if __name__ == '__main__':
    # Bloco para testar a função list_documents diretamente.
    # Este código só executa quando o script core.py é rodado diretamente.

    print(f"Procurando documentos em: {os.path.abspath(BASE_LIBRARY_PATH)}")

    # Certifique-se de que os arquivos de exemplo estão criados para este teste.
    documents = list_documents()
    if documents:
        for file_type_key, years_data in documents.items():
            print(f"\nTipo: {file_type_key.upper()}")
            for year_key, docs_list in years_data.items():
                print(f"  Ano: {year_key}")
                for doc_info in docs_list:
                    print(f"    - {doc_info['name']} (Caminho: {doc_info['path']})")
    else:
        print("Nenhum documento encontrado.")
        print("Verifique se existem arquivos de exemplo no diretório da biblioteca e se BASE_LIBRARY_PATH está correto.")
    
    # --- Testando add_document ---
    print("\n\n--- Testando a função add_document ---")
    caminho_arquivo_teste = r"c:\Users\nicol\OneDrive\Área de Trabalho\meu_novo_artigo_2025.pdf"

    if os.path.exists(caminho_arquivo_teste):
        print(f"Tentando adicionar o arquivo: {caminho_arquivo_teste}")
        sucesso, mensagem = add_document(caminho_arquivo_teste)
        print(f"Resultado da adição: {mensagem}")
        
        if sucesso:
            print("\n--- Listando documentos APÓS a tentativa de adição ---")
            documents_apos_add = list_documents() # Chama list_documents novamente
            if documents_apos_add:
                for file_type_key, years_data in documents_apos_add.items():
                    print(f"\nTipo: {file_type_key.upper()}")
                    for year_key, docs_list in years_data.items():
                        print(f"  Ano: {year_key}")
                        for doc_info in docs_list:
                            print(f"    - {doc_info['name']} (Caminho: {doc_info['path']})")
            else:
                print("Nenhum documento encontrado após a adição.")
    else:
        print(f"\nAVISO: Arquivo de teste não encontrado em '{caminho_arquivo_teste}'.")
        print("Crie este arquivo para que o teste da função add_document possa ser executado.")
    print("\n--- Testando rename_document ---")
sucesso, mensagem = rename_document("manual_de_boas_praticas_IA_2023.pdf", "guia_ia_para_bibliotecarios_2023.pdf")
print(mensagem)
