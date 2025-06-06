# Relatório de Testes do Sistema

Este documento descreve os casos de teste planejados e executados para garantir a funcionalidade e robustez do Sistema de Gerenciamento de Documentos Digitais.

## 1. Comando `list`

| Cenário de Teste | Passos para Executar | Resultado Esperado | Status |
| :--- | :--- | :--- | :--- |
| **1.1. Listar com Biblioteca Vazia** | 1. Remover todos os arquivos da biblioteca. <br> 2. Executar `python -m doc_manager.cli list` | O sistema deve exibir a mensagem "Nenhum documento encontrado na biblioteca." | ✅ Passou |
| **1.2. Listar com Biblioteca Populada** | 1. Adicionar múltiplos arquivos de tipos e anos diferentes. <br> 2. Executar `python -m doc_manager.cli list` | O sistema deve listar todos os arquivos, agrupados corretamente por tipo (PDF, EPUB, etc.) e por ano. | ✅ Passou |

## 2. Comando `add`

| Cenário de Teste | Passos para Executar | Resultado Esperado | Status |
| :--- | :--- | :--- | :--- |
| **2.1. Adicionar Novo Arquivo** | 1. Criar um arquivo de teste fora do projeto. <br> 2. Executar `python -m doc_manager.cli add "<caminho_do_arquivo>"` | Mensagem de sucesso. O arquivo deve ser copiado para a pasta `TIPO/ANO/` correta dentro da biblioteca e aparecer na listagem. | ✅ Passou |
| **2.2. Adicionar Arquivo Duplicado** | 1. Adicionar um arquivo. <br> 2. Tentar adicionar o mesmo arquivo novamente. | Mensagem de erro indicando que o arquivo já existe. O arquivo original não deve ser sobrescrito. | ✅ Passou |
| **2.3. Adicionar Arquivo Inexistente** | 1. Executar `python -m doc_manager.cli add "<caminho_falso>"` | Mensagem de erro indicando que o arquivo de origem não foi encontrado. | ✅ Passou |

## 3. Comando `rename`

| Cenário de Teste | Passos para Executar | Resultado Esperado | Status |
| :--- | :--- | :--- | :--- |
| **3.1. Renomear Arquivo com Sucesso** | 1. Escolher um arquivo existente na biblioteca. <br> 2. Executar `python -m doc_manager.cli rename "<nome_antigo>" "<nome_novo>"` | Mensagem de sucesso. Na listagem, o arquivo deve aparecer com o novo nome no mesmo local. | ✅ Passou |
| **3.2. Renomear para Nome já Existente** | 1. Escolher dois arquivos, A e B. <br> 2. Tentar renomear o arquivo A para o nome do arquivo B. | Mensagem de erro indicando que o nome de destino já existe. | ✅ Passou |
| **3.3. Renomear Arquivo Inexistente** | 1. Executar `python -m doc_manager.cli rename "<nome_falso>" "<novo_nome>"` | Mensagem de erro indicando que o arquivo a ser renomeado não foi encontrado. | ✅ Passou |
| **3.4. Renomear com Reorganização** | 1. Renomear um arquivo mudando seu ano no nome (ex: `..._2023.pdf` para `..._2024.pdf`). | Mensagem de sucesso. O arquivo deve ser movido para a pasta do novo ano (`PDF/2024/`). | ✅ Passou |

## 4. Comando `remove`

| Cenário de Teste | Passos para Executar | Resultado Esperado | Status |
| :--- | :--- | :--- | :--- |
| **4.1. Remover Arquivo com Sucesso** | 1. Escolher um arquivo existente. <br> 2. Executar `python -m doc_manager.cli remove "<nome_do_arquivo>"` | Mensagem de sucesso. O arquivo não deve mais aparecer na listagem. A pasta do ano deve ser removida se ficar vazia. | ✅ Passou |
| **4.2. Remover Arquivo Inexistente** | 1. Executar `python -m doc_manager.cli remove "<nome_falso>"` | Mensagem de erro indicando que o arquivo não foi encontrado. | ✅ Passou |

---
*Relatório gerado em 06/06/2025. Todos os testes foram executados e passaram conforme o esperado.*