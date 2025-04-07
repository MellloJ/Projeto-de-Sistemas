<h1 align="center"> Projeto-de-Sistemas | Sprint 01</h1>


<div align="center">
    <br>
    <strong>De 07/04/2024 à 04/05/2024</strong>&#x2003;
    <a href="sprint2.md">Próxima Sprint →</a><br>
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

## Sprint 01

## Valor:

Entregar as funcionalidades essenciais de autenticação e início de uso, permitindo que usuários se cadastrem, façam login e acessem a página inicial nas versões web e mobile da aplicação, viabilizando os primeiros testes de navegação e uso da plataforma.

## Features:

### **Cadastro de Usuário (Web):**
**Responsável:** João Pedro Ribeiro

**User story:** [Cadastro de Usuário](#cadastro-de-usuário) e [Cadastro de Entregador/Separador](#cadastro-de-entregadorseparador)

**Objetivo:** Implementar funcionalidade para que clientes e entregadores/separadores possam se cadastrar diretamente no site, com validação de dados e envio de documentos obrigatórios.  

### **Login de Usuário (Web):**
**Responsável:** Jônatas de Sousa Madeira

**User story:** [Login de Usuário (Cliente e Entregador/Separador)](#login-de-usuário-cliente-e-entregadorseparador)

**Objetivo:** Desenvolver autenticação segura no site, incluindo suporte a login social (Google) e funcionalidade de recuperação de senha.  

### **Cadastro de Usuário (Mobile):**
**Responsável:** Arthur Lima Duarte

**User story:** [Cadastro de Usuário](#cadastro-de-usuário) e [Cadastro de Entregador/Separador](#cadastro-de-entregadorseparador)

**Objetivo:** Criar funcionalidade no aplicativo móvel para permitir que clientes e entregadores/separadores realizem cadastro, com validação de dados e envio de documentos obrigatórios.  

### **Login de Usuário (Mobile):**
**Responsável:** Gabriel Fernandes Zamora

**User story:** [Login de Usuário (Cliente e Entregador/Separador)](#login-de-usuário-cliente-e-entregadorseparador)

**Objetivo:** mplementar autenticação segura no aplicativo móvel, com suporte a login social (Google) e opção de recuperação de senha.  

### **Página Inicial:**
**Responsável:** Jessé Eliseu Nunes Da Silva

**User story:** [Página Inicial do Sistema (Web)](#página-inicial-do-sistema-web)

**Objetivo:** Criar uma página inicial para o aplicativo, com informações básicas e opções de navegação.

---

## User Stories:

### Cadastro de Usuário

**User Story:**  
"Como um cliente, eu quero me cadastrar no aplicativo."

**Critérios de Aceitação:**  
- ✅ O usuário deve poder se cadastrar informando:
    - Nome completo  
    - Idade  
    - E-mail  
    - Telefone  
    - Senha  
- ✅ Pode haver a opção de o aplicativo perguntar se pode acessar sua localização.  
- ✅ O usuário poderá acessar o app após confirmar o cadastro imediatamente.  

**Regras de Negócio:**  
- 🔹 Caso o usuário tente se cadastrar com um e-mail já existente, o sistema deve exibir uma mensagem informando que o e-mail já está em uso.  
- 🔹 O usuário pode optar por se cadastrar usando login social (Google).  

---

### Cadastro de Entregador/Separador

**User Story:**  
"Como um entregador/separador, eu quero me cadastrar no aplicativo para poder realizar entregas ou separar compras e receber para tal."

**Critérios de Aceitação:**  
- ✅ O entregador/separador deve poder se cadastrar informando:
    - Nome completo  
    - E-mail  
    - Telefone  
    - Senha  
    - Foto  
- ✅ O sistema deve validar se o e-mail informado já está cadastrado.  
- ✅ O usuário deve enviar documentos obrigatórios (CPF, RG e/ou CNH para entregadores).  
- ✅ Para entregadores, deve ser informada a placa do veículo (caso utilize um).  
- ✅ Após o cadastro, o usuário deve receber um feedback de confirmação e um nome de usuário como entregador para acessar sua conta.  
- ✅ O login do usuário será liberado na plataforma após a aprovação dos documentos pela equipe administrativa.  

**Regras de Negócio:**  
- 🔹 O cadastro deve ser feito apenas por maiores de 18 anos.  
- 🔹 Caso o usuário tente se cadastrar com um e-mail já existente, o sistema deve exibir uma mensagem informando que o e-mail já está em uso.  
- 🔹 O usuário pode optar por se cadastrar usando login social (Google/Apple), mas ainda precisará enviar documentos para aprovação.  
- 🔹 O tempo médio de aprovação de cadastro deve ser informado ao usuário no momento da inscrição.  

---

### Login de Usuário (Cliente e Entregador/Separador)

**User Story:**  
"Como um usuário (cliente ou entregador/separador), eu quero acessar minha conta no aplicativo de forma segura para utilizar os serviços disponíveis, além de me manter logado."

**Critérios de Aceitação:**  
- ✅ O usuário deve poder fazer login utilizando nome/e-mail e senha cadastrados.  
- ✅ O sistema deve validar as credenciais e exibir uma mensagem de erro caso estejam incorretas.  
- ✅ O usuário pode optar por fazer login com autenticação social (Google/Apple).  
- ✅ Caso o usuário esqueça a senha, deve haver uma opção para recuperação via e-mail ou SMS.  
- ✅ Para garantir a segurança, o sistema pode solicitar autenticação em dois fatores (2FA) para logins suspeitos.  
- ✅ Para entregadores/separadores sem os dados validados, ainda não poderão acessar o aplicativo.  

**Regras de Negócio:**  
- 🔹 O login deve ser único para ambos os perfis (cliente e entregador/separador), diferenciando a experiência após a autenticação.  
- 🔹 O sistema deve lembrar a sessão do usuário, permitindo login automático em dispositivos confiáveis.  
- 🔹 Se um usuário for bloqueado ou estiver com documentos pendentes (no caso de entregadores/separadores), o sistema deve exibir uma mensagem informando o motivo.  
- 🔹 O armazenamento de senhas deve seguir padrões de segurança (hash e criptografia).  

### Página Inicial do Sistema (Web)

**User Story:**  
"Como um usuário autenticado ou não autenticado, quero poder acessar a URL inicial do site e visualizar informações básicas."

**Critérios de Aceitação:**  
- ✅ A página inicial deve ser acessível tanto em computadores quanto em dispositivos móveis.  
- ✅ Deve exibir informações claras para que o usuário possa realizar login e/ou cadastro no sistema.  

**Regras de Negócio:**  
- 🔹 A página inicial deve ser responsiva, adaptando-se a diferentes tamanhos de tela.  
- 🔹 Deve conter links ou botões para redirecionar o usuário para as páginas de login e cadastro.  
- 🔹 Caso o usuário já esteja autenticado, a página inicial deve exibir informações personalizadas, como nome e opções de navegação para funcionalidades disponíveis.  
