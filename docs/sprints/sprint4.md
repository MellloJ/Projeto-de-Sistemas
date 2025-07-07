<h1 align="center"> Projeto-de-Sistemas | Sprint 04</h1>

<div align="center">
    <br>
    <a href="sprint3.md">← Sprint Anterior </a>&#x2003;
    <strong>De 02/06/2024 à 15/06/2024</strong>&#x2003;<br>
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

## Sprint 04

## Valor:

Entregar funcionalidades completas para os perfis de separador e entregador, viabilizando a operação prática de pedidos dentro da aplicação. Incluir o gerenciamento de notificações e pedidos em tempo real, além de implementar a base para administração de usuários e controle de entregas no sistema.

---

## Features:

### **API para retornar dados de separador e entregador**
**Responsável:** João Pedro Ribeiro (Gameplays)

**User story:** [Visualização de Perfil de Separador/Entregador](#visualização-de-perfil-de-separadorentregador)

**Objetivo:** Criar uma API que retorne os dados dos usuários com perfil de separador ou entregador, permitindo o carregamento das informações pessoais no painel ou app.

---

### **Token FCM e envio de notificação**
**Responsável:** Jônatas de Sousa Madeira (Jotta)

**User story:** [Notificações para entregadores](#notificações-para-entregadores)

**Objetivo:** Implementar o armazenamento e atualização de tokens do Firebase Cloud Messaging (FCM) no backend, e enviar notificações push para entregadores quando o pedido estiver pronto para entrega.

---

### **Listar pedidos de um usuário**
**Responsável:** João Pedro Ribeiro (Gameplays)

**User story:** [Histórico e pedidos em andamento](#histórico-e-pedidos-em-andamento)

**Objetivo:** Criar endpoint para listar todos os pedidos realizados por um usuário, com filtros por status e ordenação por data.

---

### **Funcionalidade de Entrega (API + Tabela)**
**Responsável:** Jônatas de Sousa Madeira (Jotta)

**User story:** [Gestão de entregas](#gestão-de-entregas)

**Objetivo:** Criar tabela e endpoints no backend para registrar e atualizar informações sobre entregas realizadas, status atual e entregadores responsáveis.

---

### **Painel Administrativo**
**Responsável:** Jessé Eliseu Nunes Da Silva

**User story:** [Administração do sistema](#administração-do-sistema)

**Objetivo:** Desenvolver uma interface administrativa para gerenciar usuários, serviços e validação de documentos enviados pelos entregadores e separadores.

---

## App (Mobile)

### **Separador**

#### **Home / Visão Geral**
**Responsável:** Arthur Lima

**Objetivo:** Exibir um dashboard com o resumo das atividades do separador, incluindo número de pedidos pendentes, mercado atual e status gerais.

#### **Receber mercado atribuído**
**Responsável:** Arthur Lima

**Objetivo:** Exibir o mercado atual em que o separador está trabalhando, com dados como nome, endereço e lista de produtos a serem separados.

#### **Marcar produtos como separados**
**Responsável:** Arthur Lima

**Objetivo:** Permitir ao separador atualizar o status dos produtos no pedido conforme forem separados, com integração direta à API.

#### **Solicitações de separação**
**Responsável:** Arthur Lima

**Objetivo:** Criar tela listando as solicitações de separação com filtros por status (pendente, em andamento, concluído), consumindo os dados da API de pedidos.

#### **Perfil / Logout / Navegação entre áreas**
**Responsável:** Arthur Lima

**Objetivo:** Implementar tela de perfil com dados pessoais, botão de logout e possibilidade de alternar entre as áreas de cliente, separador e entregador (se aplicável).

---

### **Entregador**

#### **Solicitações de entrega**
**Responsável:** Gabriel Fernandes

**Objetivo:** Criar tela que exibe as entregas atribuídas ao entregador, com detalhes como endereço, horário, e status do pedido.

#### **GPS / Rota de Entrega**
**Responsável:** Gabriel Fernandes

**Objetivo:** Exibir rota para o local de entrega usando integração com biblioteca de mapas (Google Maps API ou similar).

#### **Home / Visão Geral**
**Responsável:** Gabriel Fernandes

**Objetivo:** Apresentar um resumo das entregas pendentes, entregas em andamento e atividades recentes do entregador.

#### **Perfil / Login / Logout / Navegação**
**Responsável:** Gabriel Fernandes

**Objetivo:** Implementar gerenciamento do perfil do entregador, com funcionalidades de login, logout e transição entre perfis (cliente/entregador).

#### **Histórico de Entregas**
**Responsável:** Gabriel Fernandes

**Objetivo:** Exibir histórico de entregas realizadas pelo entregador, integrando-se com nova API que consultará dados persistidos no banco de dados.

---

## User Stories

### Visualização de Perfil de Separador/Entregador

**User Story:**  
"Como separador ou entregador, quero acessar meus dados pessoais e operacionais para visualizar meu perfil e acompanhar minhas atividades."

**Critérios de Aceitação:**  
- ✅ Deve retornar nome, e-mail, tipo de usuário, e dados operacionais associados.  
- ✅ Dados devem estar atualizados com o cadastro aprovado.  

**Regras de Negócio:**  
- 🔹 Apenas usuários autenticados podem visualizar essas informações.  
- 🔹 Dados sensíveis devem ser protegidos (como CPF e documentos).  

---

### Notificações para Entregadores

**User Story:**  
"Como entregador, quero receber uma notificação push quando um pedido estiver pronto, para agilizar a coleta e entrega."

**Critérios de Aceitação:**  
- ✅ O token FCM deve ser salvo e atualizado no backend.  
- ✅ A notificação deve ser enviada automaticamente quando o pedido mudar para status 'Pronto para entrega'.  

**Regras de Negócio:**  
- 🔹 Notificações só devem ser enviadas para entregadores logados com token válido.  
- 🔹 É necessário manter uma fila de notificações para controle de entregas em lote.  

---

### Histórico e Pedidos em Andamento

**User Story:**  
"Como cliente, quero acessar o histórico dos meus pedidos e acompanhar os pedidos em andamento."

**Critérios de Aceitação:**  
- ✅ Listar pedidos por data, com status atual.  
- ✅ Deve permitir filtros (entregue, em andamento, cancelado).  

**Regras de Negócio:**  
- 🔹 O usuário precisa estar autenticado.  
- 🔹 Pedidos devem ser atualizados em tempo real conforme eventos de separação e entrega.  

---

### Gestão de Entregas

**User Story:**  
"Como administrador do sistema, quero registrar e acompanhar as entregas feitas pelos entregadores."

**Critérios de Aceitação:**  
- ✅ Criar estrutura no banco para salvar entregas com status, data e entregador.  
- ✅ A API deve permitir atualização do status (em rota, entregue).  

**Regras de Negócio:**  
- 🔹 Apenas entregadores aprovados podem ter entregas atribuídas.  
- 🔹 Status da entrega afeta o histórico do entregador.  

---

### Administração do Sistema

**User Story:**  
"Como administrador, quero poder visualizar e gerenciar todos os usuários, serviços e documentos enviados para manter a organização da plataforma."

**Critérios de Aceitação:**  
- ✅ Deve permitir bloquear, ativar ou editar usuários.  
- ✅ Validar documentos enviados pelos entregadores/separadores.  

**Regras de Negócio:**  
- 🔹 Apenas administradores autenticados podem acessar esse painel.  
- 🔹 Toda alteração deve ser registrada no histórico de ações administrativas.