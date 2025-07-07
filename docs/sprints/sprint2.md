<h1 align="center"> Projeto-de-Sistemas | Sprint 02</h1>

<div align="center">
    <br>
    <a href="sprint1.md">← Sprint Anterior </a>&#x2003;
    <strong>De 05/05/2024 à 18/05/2024</strong>&#x2003;
    <a href="sprint3.md">Próxima Sprint →</a><br>
    <br>
</div>

<table align="center">
    <tr>
        <td><a href="../../README.md">Home</a></td>
        <td><a href="../defaults.md">Padrões</a></td>
        <td><a href="../plan.md">Planejamento</a></td>
        <td><a href="../us.md">Quem Somos</a></td>
        <td>
            <details style="position: relative;">
                <summary>Mais</summary>
                <ul style="position: absolute; background: transparent;">
                    <li><a href="../contact.md">Contato</a></li>
                    <li><a href="../sup.md">Suporte</a></li>
                    <li><a href="../faq.md">FAQ</a></li>
                </ul>
            </details>
        </td>
    </tr>
</table>

<hr>

<h1>Sprint 02</h1>

<h2>Valor:</h2>
<p>
Entregar funcionalidades fundamentais para garantir a segurança de acesso, facilitar a pesquisa de produtos e estruturar a navegação inicial dos usuários, tanto na plataforma web quanto mobile, permitindo o início da personalização da experiência dentro do aplicativo.
</p>

<h2>Features:</h2>

<h3><strong>Implementação de Autenticação JWT (Web)</strong></h3>
<p><strong>Responsável:</strong> Jônatas de Sousa Madeira</p>
<p><strong>User Story:</strong> <a href="#implementacao-de-autenticacao-segura">Implementação de Autenticação Segura</a></p>
<p><strong>Objetivo:</strong><br>
Implementar autenticação utilizando JWT (JSON Web Tokens) para garantir sessões seguras e protegidas, permitindo que apenas usuários autenticados possam acessar rotas privadas da aplicação web.
</p>

<hr>

<h3><strong>Filtro de Pesquisa de Produtos (Web)</strong></h3>
<p><strong>Responsável:</strong> Jessé Eliseu Nunes Da Silva</p>
<p><strong>User Story:</strong> <a href="#filtro-de-pesquisa-de-produtos">Filtro de Pesquisa de Produtos</a></p>
<p><strong>Objetivo:</strong><br>
Desenvolver funcionalidade de pesquisa para que usuários possam localizar produtos facilmente, com filtros aplicáveis por nome, categoria, preço e outras características relevantes.
</p>

<hr>

<h3><strong>Home com Lista de Itens (Mobile)</strong></h3>
<p><strong>Responsável:</strong> Arthur Lima Duarte</p>
<p><strong>User Story:</strong> <a href="#home-com-lista-de-itens">Home com Lista de Itens</a></p>
<p><strong>Objetivo:</strong><br>
Criar a página inicial do aplicativo mobile, exibindo uma lista de itens disponíveis para visualização, com design responsivo e intuitivo para facilitar a navegação dos usuários.
</p>

<hr>

<h3><strong>Dashboard com Perfil Editável (Mobile)</strong></h3>
<p><strong>Responsável:</strong> Gabriel Fernandes Zamora</p>
<p><strong>User Story:</strong> <a href="#dashboard-do-usuario">Dashboard do Usuário</a></p>
<p><strong>Objetivo:</strong><br>
Desenvolver um painel de controle dentro do aplicativo mobile onde o usuário possa visualizar e editar suas informações de perfil, como nome, e-mail e senha.
</p>

<hr>

<h2>User Stories:</h2>

<h3 id="implementacao-de-autenticacao-segura">Implementação de Autenticação Segura</h3>
<p><strong>User Story:</strong><br>
"Como um usuário, eu quero acessar a plataforma de forma segura, garantindo que meus dados estejam protegidos."
</p>

<h4>Critérios de Aceitação:</h4>
<ul>
<li>✅ Implementação de login utilizando JWT.</li>
<li>✅ Geração de token após login bem-sucedido.</li>
<li>✅ Validação automática de token em rotas protegidas.</li>
<li>✅ Expiração segura dos tokens para reforçar a segurança.</li>
</ul>

<h4>Regras de Negócio:</h4>
<ul>
<li>🔹 A autenticação deve ser obrigatória para acessar áreas privadas.</li>
<li>🔹 Tokens devem ser gerados apenas após validação de credenciais corretas.</li>
<li>🔹 Tokens expirados devem impedir o acesso, forçando novo login.</li>
</ul>

<hr>

<h3 id="filtro-de-pesquisa-de-produtos">Filtro de Pesquisa de Produtos</h3>
<p><strong>User Story:</strong><br>
"Como um usuário, quero pesquisar produtos no site aplicando filtros para encontrar o que preciso com facilidade."
</p>

<h4>Critérios de Aceitação:</h4>
<ul>
<li>✅ Permitir busca por nome de produto.</li>
<li>✅ Permitir aplicação de filtros por categorias.</li>
<li>✅ Permitir ordenação por preço ou relevância.</li>
<li>✅ Interface de filtros fácil de usar, sem recarregar a página.</li>
</ul>

<h4>Regras de Negócio:</h4>
<ul>
<li>🔹 Os filtros devem retornar resultados precisos e relevantes.</li>
<li>🔹 Caso não haja produtos para a pesquisa, uma mensagem apropriada deve ser exibida.</li>
</ul>

<hr>

<h3 id="home-com-lista-de-itens">Home com Lista de Itens</h3>
<p><strong>User Story:</strong><br>
"Como um usuário do app mobile, quero ver uma lista de itens logo ao abrir o aplicativo para começar a navegar imediatamente."
</p>

<h4>Critérios de Aceitação:</h4>
<ul>
<li>✅ Exibir lista de produtos ou itens na tela inicial.</li>
<li>✅ Layout responsivo e adaptado para diferentes tamanhos de tela.</li>
<li>✅ Permitir clique em um item para mais detalhes.</li>
</ul>

<h4>Regras de Negócio:</h4>
<ul>
<li>🔹 A lista de itens deve ser carregada rapidamente para boa experiência do usuário.</li>
<li>🔹 Itens exibidos podem ser atualizados dinamicamente conforme novas entradas.</li>
</ul>

<hr>

<h3 id="dashboard-do-usuario">Dashboard do Usuário</h3>
<p><strong>User Story:</strong><br>
"Como usuário, quero acessar meu perfil e editar minhas informações pessoais diretamente pelo aplicativo mobile."
</p>

<h4>Critérios de Aceitação:</h4>
<ul>
<li>✅ Visualizar informações como nome, e-mail e telefone no dashboard.</li>
<li>✅ Editar e salvar informações pessoais diretamente pela interface.</li>
<li>✅ Mensagem de confirmação após alteração bem-sucedida.</li>
</ul>

<h4>Regras de Negócio:</h4>
<ul>
<li>🔹 A alteração de dados deve ser validada (ex.: formato de e-mail correto).</li>
<li>🔹 Alterações sensíveis, como senha, devem exigir confirmação adicional (ex.: digitar senha atual).</li>
</ul>

