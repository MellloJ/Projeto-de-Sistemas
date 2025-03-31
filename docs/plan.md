<h1 align="center"> Projeto-de-Sistemas | Planejamento</h1>

<table align="center">
    <tr>
        <td><a href="../README.md">Home</a></td>
        <td><a href="defaults.md">Padrões</a></td>
        <td>Planejamento</td>
        <td><a href="us.md">Quem Somos</a></td>
        <td>
            <details style="position: relative;">
                <summary>Mais</summary>
                <ul style="position: absolute; background: transparent;">
                    <li><a href="contact.md">Contato</a></li>
                    <li><a href="sup.md">Suporte</a></li>
                    <li><a href="faq.md">FAQ</a></li>
                </ul>
            </details>
        </td>
    </tr>
</table>

<hr>

## Para o projeto:

- Utilizar autenticação [JWT (Json Web Token)](https://www.totvs.com/blog/gestao-para-assinatura-de-documentos/jwt-token/) para todas as requisições do projeto desde o começo.
- Escrever os arquivos de [teste](https://docs-djangoproject-com.translate.goog/en/5.1/topics/testing/?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt&_x_tr_pto=tc) para cada funcionalidade nova.
- Tenha [Node.js](https://nodejs.org/pt/download) Instalado.

### Padrões Django para a aplicação WEB:

- [Service Layer](https://breadcrumbscollector.tech/how-to-implement-a-service-layer-in-django-rest-framework/) (Camada de Serviço)
- [Repository patterns](https://medium.com/@slowmoe329/repository-design-pattern-in-django-a-clean-and-scalable-approach-a94d2645fd77)
- Arquitetura Modular (Divisão de [Apps](https://docs-djangoproject-com.translate.goog/en/5.1/ref/applications/?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt&_x_tr_pto=wa))

### Configurando banco de dados:

Se não estiver instalado, instale o [Docker](https://www.docker.com/get-started/).

#### Primeira vez:
1. Certifique-se de estar no diretório base do projeto.
2. Abra um novo terminal e execute o comando abaixo para iniciar o container do banco de dados:
    ```bash
    docker-compose up
    ```
3. Verifique se o container está em execução (outro terminal):
    ```bash
    docker ps
    ```
4. Configure as variáveis de ambiente no seu arquivo `.env`:
    ```
    DATABASE_NAME=nome_do_banco
    DATABASE_USER=usuario
    DATABASE_PASSWORD=senha
    DATABASE_HOST=localhost
    DATABASE_PORT=5432
    ```

#### Iniciando o container existente:

Para ver todos os containers existentes, use o comando: `docker ps -a`

1. Certifique-se de estar no diretório base do projeto.
2. Para iniciar um container que já foi criado anteriormente,abra um novo terminal e use o comando:
    ```bash
    docker start nome_do_container
    ```
3. Verifique se o container está em execução (outro terminal):
    ```bash
    docker ps
    ```

#### Parando o container:
1. Para parar o container em execução, use o comando:
    ```bash
    docker stop nome_do_container
    ```
### Configurando o Dbeaver

1. Instale o [Dbeaver Community](https://dbeaver.io/download/) e execute.
   
2. Clique para criar uma nova conexão:
   ![Group 1](https://github.com/user-attachments/assets/344c06a8-ccfd-408a-949b-1c3e6d18eabd)
   
3. Selecione **PostregeSQL** e clique em **concluir**
   ![Group 2](https://github.com/user-attachments/assets/db00db5e-ebf3-4d24-9787-7ed61a0a1dcb)

4. Clique em **Exibir todos bancos de dados**, defina o **Nome de usuário** para: **root** e a **Senha** para: **1**
    ![Group 3](https://github.com/user-attachments/assets/c156b91a-f6cb-4641-95ad-6d38adf8eed6)



## Sprints:

| Sprint | Data de Início | Data de Término | Link                     |
|--------|----------------|-----------------|--------------------------|
| 1      | 07/04/2024     | 04/05/2024      | [Detalhes](sprints/sprint1.md)  |
| 2      | 05/05/2024     | 18/05/2024      | [Detalhes](sprints/sprint2.md)  |
| 3      | 19/05/2024     | 01/06/2024      | [Detalhes](sprints/sprint3.md)  |
| 4      | 02/06/2024     | 15/06/2024      | [Detalhes](sprints/sprint4.md)  |
