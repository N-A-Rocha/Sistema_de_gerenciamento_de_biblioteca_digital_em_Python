# Guia de Contribuição

Ficamos felizes com o seu interesse em contribuir para o Sistema de Gerenciamento de Documentos Digitais! Para manter o projeto organizado, pedimos que siga as seguintes diretrizes.

## Fluxo de Trabalho com Pull Requests

Todas as alterações no projeto, desde novas funcionalidades a correções de bugs e melhorias na documentação, devem ser feitas através de Pull Requests. A branch `main` está protegida e não aceita pushes diretos.

O processo é o seguinte:

1.  **Crie uma Nova Branch:** A partir da versão mais atualizada da branch `main`, crie uma nova branch local para trabalhar na sua alteração. Use um nome descritivo, prefixado com o tipo de alteração.
    * Para novas funcionalidades: `feat/nome-da-funcionalidade` (ex: `feat/adicionar-campo-autor`)
    * Para correções de bugs: `fix/descricao-do-bug` (ex: `fix/erro-ao-renomear-arquivo`)
    * Para documentação: `docs/o-que-foi-documentado` (ex: `docs/atualiza-readme`)

    ```bash
    # Garanta que sua main local está atualizada
    git checkout main
    git pull origin main

    # Crie sua nova branch
    git checkout -b feat/minha-nova-funcionalidade
    ```

2.  **Faça seus Commits:** Trabalhe na sua alteração e faça commits pequenos e lógicos. As mensagens de commit devem seguir o padrão de Commits Convencionais.
    * **Formato:** `<tipo>(<escopo>): <descrição>`
    * **Exemplos:**
        * `feat(core): Implementa função remove_document`
        * `fix(cli): Corrige texto de ajuda do comando add`
        * `docs: Adiciona guia de contribuição`

    ```bash
    git add .
    git commit -m "feat(cli): Adiciona novo comando 'search'"
    ```

3.  **Envie sua Branch para o GitHub (`push`):**
    Quando estiver pronto, envie sua branch de funcionalidade para o repositório remoto.

    ```bash
    git push -u origin feat/minha-nova-funcionalidade
    ```

4.  **Abra um Pull Request:**
    * Vá para a página do repositório no GitHub.
    * Você verá um aviso para criar um Pull Request a partir da sua nova branch. Clique em "Compare & pull request".
    * Dê um título claro para o seu Pull Request e uma descrição do que foi feito e por quê.
    * Crie o Pull Request.

Agradecemos sua contribuição!