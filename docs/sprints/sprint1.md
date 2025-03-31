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