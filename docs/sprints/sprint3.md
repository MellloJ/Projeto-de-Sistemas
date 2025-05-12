<h1 align="center"> Projeto-de-Sistemas | Sprint 03</h1>

<div align="center">
    <br>
    <a href="sprint2.md">← Sprint Anterior </a>&#x2003;
    <strong>De 19/05/2024 à 01/06/2024</strong>&#x2003;
    <a href="sprint4.md">Próxima Sprint →</a><br>
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

# Sprint 03

## Valor:

Ampliar as funcionalidades da plataforma, permitindo que os usuários tenham acesso a mais recursos do sistema, como visualização de produtos por mercado, adição de endereços, e integração de processos operacionais com entregadores e separadores, além de preparar o app para lidar com pedidos e pagamentos.

## Features:

### **API de Usuários:**

**Responsável:** João Pedro Ribeiro

**User story:** [Gerenciamento de Usuário](#gerenciamento-de-usuário)

**Objetivo:** Criar endpoints para retornar, editar e excluir os dados dos usuários, permitindo a gestão completa do perfil pela interface administrativa e pelo próprio usuário.

### **API de Endereços dos Usuários:**

**Responsável:** João Pedro Ribeiro

**User story:** [Cadastro de Endereços](#cadastro-de-endereços)

**Objetivo:** Implementar uma API para que os usuários possam adicionar, editar ou remover endereços de entrega vinculados à sua conta.

### **API de Cadastro de Entregador:**

**Responsável:** Jônatas de Sousa Madeira

**User story:** [Cadastro de Entregador/Separador](#cadastro-de-entregadorseparador)

**Objetivo:** Criar endpoint para cadastrar entregadores no sistema com validação de dados, documentos obrigatórios e vínculo com o sistema de pedidos.

### **API de Cadastro de Separador:**

**Responsável:** Jônatas de Sousa Madeira

**User story:** [Cadastro de Entregador/Separador](#cadastro-de-entregadorseparador)

**Objetivo:** Implementar uma API para permitir o cadastro de separadores de mercado, incluindo os dados necessários para vinculação com mercados específicos.

### **API de Mercados e Produtos:**

**Responsável:** Jessé Eliseu Nunes Da Silva

**User story:** [Listagem de Produtos por Mercado](#listagem-de-produtos-por-mercado)

**Objetivo:** Desenvolver uma API que retorne os dados dos mercados cadastrados, incluindo os produtos disponíveis, quantidade e informações de disponibilidade.

### **Relacionamento Mercado/Produto:**

**Responsável:** Jessé Eliseu Nunes Da Silva

**User story:** [Listagem de Produtos por Mercado](#listagem-de-produtos-por-mercado)

**Objetivo:** Estruturar e normalizar o banco de dados para associar corretamente os produtos aos mercados que os oferecem, garantindo integridade e flexibilidade nas buscas.

---

## App:

### **Pedidos no App:**

**Responsável:** Arthur Lima Duarte

**User story:** [Pedidos no Aplicativo](#pedidos-no-aplicativo)

**Objetivo:** Implementar no app a lógica para exibir os pedidos feitos pelos clientes, consumindo os dados da API de pedidos.

### **Pagamentos:**

**Responsável:** Arthur Lima Duarte

**User story:** [Pagamento pelo Aplicativo](#pagamento-pelo-aplicativo)

**Objetivo:** Adicionar funcionalidade de pagamento dentro do app, integrando com uma plataforma de pagamento (ex: Pix, cartão) de forma segura.

### **Chamar Entregador:**

**Responsável:** Gabriel Fernandes Zamora

**User story:** [Chamar Entregador](#chamar-entregador)

**Objetivo:** Criar a lógica para, ao concluir um pedido, notificar o entregador disponível mais próximo para realizar a entrega.

### **Tela de Mercados:**

**Responsável:** Arthur Lima Duarte

**User story:** [Listagem de Produtos por Mercado](#listagem-de-produtos-por-mercado)

**Objetivo:** Criar uma tela no app para listar os mercados disponíveis, com seus respectivos produtos, facilitando a navegação e escolha do cliente.

### **Tela de Produto Detalhado:**

**Responsável:** Gabriel Fernandes Zamora

**User story:** [Exibição de Dados do Produto](#exibição-de-dados-do-produto)

**Objetivo:** Desenvolver uma interface para mostrar os detalhes do produto selecionado, com informações como descrição, preço e disponibilidade.

---

## User Stories:

### Gerenciamento de Usuário

**User Story:**
"Como um usuário, quero visualizar e atualizar meus dados cadastrados para manter minhas informações atualizadas."

**Critérios de Aceitação:**

* ✅ Usuário pode editar nome, e-mail, senha e telefone.
* ✅ Os dados são atualizados em tempo real com confirmação visual.
* ✅ Caso o e-mail já exista, o sistema deve alertar o usuário.

---

### Cadastro de Endereços

**User Story:**
"Como um cliente, quero cadastrar meus endereços para que as entregas sejam feitas corretamente."

**Critérios de Aceitação:**

* ✅ O usuário deve informar CEP, rua, número, complemento (opcional), bairro e cidade.
* ✅ Pode ter mais de um endereço cadastrado.
* ✅ O sistema deve validar os campos obrigatórios.

---

### Cadastro de Entregador/Separador

**User Story:**
"Como um entregador/separador, quero me cadastrar no sistema para realizar entregas ou separações de pedidos."

**Critérios de Aceitação:**

* ✅ Informar nome completo, e-mail, telefone, senha e documentos obrigatórios.
* ✅ Sistema valida a idade mínima (18 anos) e verifica se o e-mail já está cadastrado.
* ✅ Após o cadastro, o status fica como 'pendente' até aprovação.

---

### Listagem de Produtos por Mercado

**User Story:**
"Como um cliente, quero visualizar os produtos disponíveis em cada mercado, com informações como preço e quantidade."

**Critérios de Aceitação:**

* ✅ A listagem deve conter nome, preço e quantidade de cada produto.
* ✅ Produtos devem estar associados a um mercado específico.
* ✅ Deve ser possível filtrar ou buscar produtos.

---

### Pedidos no Aplicativo

**User Story:**
"Como um cliente, quero ver meus pedidos dentro do aplicativo."

**Critérios de Aceitação:**

* ✅ Os pedidos devem mostrar status (em preparação, em rota, entregue).
* ✅ O histórico de pedidos anteriores deve estar acessível.

---

### Pagamento pelo Aplicativo

**User Story:**
"Como um cliente, quero pagar meus pedidos pelo app com segurança."

**Critérios de Aceitação:**

* ✅ Pode escolher forma de pagamento (Pix, cartão).
* ✅ Sistema confirma pagamento antes de encaminhar pedido.

---

### Chamar Entregador

**User Story:**
"Como sistema, quero notificar o entregador quando um pedido estiver pronto para entrega."

**Critérios de Aceitação:**

* ✅ Sistema deve localizar entregador mais próximo disponível.
* ✅ Entregador deve receber notificação com dados do pedido e cliente.

---

### Exibição de Dados do Produto

**User Story:**
"Como um cliente, quero ver detalhes do produto antes de comprar."

**Critérios de Aceitação:**

* ✅ Tela deve exibir nome, imagem, descrição e preço do produto.
* ✅ Deve ter botão para adicionar ao carrinho.