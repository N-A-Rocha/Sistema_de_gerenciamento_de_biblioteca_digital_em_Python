# Sistema de Gerenciamento de Documentos Digitais

Repositório para o projeto de Programação para Ciência de Dados (Hora da Prática 2).

Este projeto é um sistema de linha de comando (CLI) em Python, desenvolvido para uma biblioteca universitária, com o objetivo de facilitar a gestão de uma vasta coleção de artigos, teses e livros em formatos digitais. O sistema automatiza a organização e manipulação dos arquivos, substituindo um processo manual ineficiente e propenso a erros.

---

## ✨ Funcionalidades

O sistema oferece as seguintes operações via linha de comando:

* **`list`**: Lista todos os documentos na biblioteca, organizados por tipo de arquivo e ano de publicação.
    * Inclui uma opção `-v` ou `--verbose` para uma visualização detalhada com o caminho completo de cada arquivo.
* **`add`**: Adiciona um novo documento à biblioteca a partir de um caminho de origem. O sistema organiza o arquivo automaticamente em uma estrutura de pastas `TIPO/ANO/`.
* **`rename`**: Renomeia um documento existente. Se o novo nome alterar o tipo ou o ano do arquivo, o sistema o move automaticamente para a pasta correta.
* **`remove`**: Remove um documento da biblioteca, com um prompt de confirmação para evitar deleções acidentais.

---

## 🚀 Como Usar

### Pré-requisitos
* Python 3.x

### Instalação
1.  Clone este repositório:
    ```bash
    git clone [https://github.com/N-A-Rocha/Sistema_de_gerenciamento_de_biblioteca_digital_em_Python.git](https://github.com/N-A-Rocha/Sistema_de_gerenciamento_de_biblioteca_digital_em_Python.git)
    ```
2.  Navegue até o diretório do projeto:
    ```bash
    cd Sistema_de_gerenciamento_de_biblioteca_digital_em_Python
    ```
3.  Atualmente, o projeto não possui dependências externas. Se fossem adicionadas, a instalação seria feita com `pip install -r requirements.txt`.

### Execução dos Comandos

Todos os comandos devem ser executados a partir da pasta raiz do projeto.

* **Listar documentos (simples):**
    ```bash
    python -m doc_manager.cli list
    ```
* **Listar documentos (detalhado):**
    ```bash
    python -m doc_manager.cli list --verbose
    ```
* **Adicionar um documento:**
    ```bash
    python -m doc_manager.cli add "Caminho/completo/para/seu/documento.pdf"
    ```
* **Renomear um documento:**
    ```bash
    python -m doc_manager.cli rename "nome_antigo.pdf" "nome_novo_2024.pdf"
    ```
* **Remover um documento:**
    ```bash
    python -m doc_manager.cli remove "nome_do_arquivo_a_remover.pdf"
    ```

---

## 📂 Estrutura do Projeto

Sistema_de_gerenciamento_de_biblioteca_digital_em_Python/
├── doc_manager/              # Pacote principal com a lógica da aplicação
│   ├── core.py               # Funções principais (lógica de negócio)
│   └── cli.py                # Lógica da Interface de Linha de Comando (CLI)
├── digital_library_files/    # Diretório onde os documentos são armazenados
├── .gitignore                # Arquivos e pastas a serem ignorados pelo Git
├── CONTRIBUTING.md           # Guia para contribuições ao projeto
├── README.md                 # Este arquivo
└── TESTES.md                 # Relatório de testes das funcionalidades

---


## 🤝 Contribuição

Contribuições são bem-vindas! Por favor, leia nosso [Guia de Contribuição](CONTRIBUTING.md) para entender nosso fluxo de trabalho com Pull Requests.

---

### **Nota sobre a Proteção da Branch `main`**

Foi configurado um "Ruleset" no GitHub para proteger a branch `main`, exigindo Pull Requests para todas as alterações, conforme as boas práticas de desenvolvimento. Devido a uma limitação do GitHub para repositórios privados em contas pessoais gratuitas, a aplicação forçada desta regra não está ativa.

No entanto, para fins de demonstração de um fluxo de trabalho profissional e para garantir a qualidade do código, **todas as contribuições a este projeto seguirão estritamente o fluxo de trabalho com Pull Requests.**