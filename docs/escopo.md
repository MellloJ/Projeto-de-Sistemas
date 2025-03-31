<h1 align="center"> Projeto-de-Sistemas | Escopo</h1>

<table align="center">
    <tr>
        <td><a href="../README.md">Home</a></td>
        <td><a href="defaults.md">Padrões</a></td>
        <td><a href="plan.md">Planejamento</a></td>
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

## Escopo do Projeto

### **1. Objetivo do Sistema**
O sistema tem como objetivo conectar clientes e entregadores/separadores para facilitar a realização de serviços como entrega de produtos e separação de compras. Ele deve oferecer uma experiência segura, eficiente e intuitiva para todos os usuários.

---

### **2. Funcionalidades Principais**
- **Cadastro de Usuários:** Permitir que clientes e entregadores/separadores se cadastrem com validação de dados e envio de documentos.
- **Login e Autenticação:** Login seguro com suporte a autenticação social (Google) e recuperação de senha.
- **Gestão de Serviços:** Solicitação de serviços por clientes e aceitação por entregadores/separadores.
- **Notificações:** Envio de atualizações em tempo real sobre status de serviços.
- **Administração:** Painel administrativo para gerenciar usuários, serviços e documentos.

---

### **3. Requisitos Funcionais**
- O sistema deve permitir que clientes solicitem serviços e acompanhem o status em tempo real.
- Entregadores/separadores devem poder enviar documentos e aguardar aprovação.
- O sistema deve validar e-mails duplicados e documentos obrigatórios.

---

### **4. Requisitos Não Funcionais**
<!-- - O sistema deve suportar até 1.000 usuários simultâneos. -->
- Garantir tempo de resposta inferior a 2 segundos para operações comuns.
- As senhas devem ser armazenadas com hash seguro.

---

### **5. Tecnologias Utilizadas**
- **Backend:** Django (Python)  
- **Frontend:** Tailwind CSS para estilização e templates Django para renderização.  
- **Mobile:** Flutter para desenvolvimento do aplicativo mobile.  
- **Outros:** Git para controle de versão, Trello para gerenciamento de tarefas, Lucidchart para criação de diagramas, Figma para design de interfaces.    

---

### **6. Usuários e Perfis de Acesso**
- **Clientes:** Podem solicitar serviços e acompanhar status.
- **Entregadores/Separadores:** Podem aceitar serviços e gerenciar documentos.
- **Administradores:** Gerenciam usuários, documentos e serviços.

---

### **7. Escopo de Exclusão**
- Integração com redes sociais além de login social (Google) não serão implementadas na primeira versão.
- Funcionalidades avançadas de relatórios e análises não serão implementada na primeira versão.
- Não haverá suporte a pagamentos online na primeira versão.
- O sistema não incluirá funcionalidades de geolocalização na primeira versão.
- Não haverá suporte a múltiplos idiomas na primeira versão.
- Funcionalidades de chat em tempo real entre usuários não serão implementadas na primeira versão.
- O sistema não incluirá funcionalidades de feedback ou avaliações entre usuários na primeira versão.
- O sistema não incluirá funcionalidades de backup automático na primeira versão.
- Funcionalidades de relatórios avançados e análises de dados não serão implementadas na primeira versão.
- O sistema não incluirá funcionalidades de personalização de interface para usuários na primeira versão.

---

### **8. Cronograma de Desenvolvimento**
- **Sprint 01:** Cadastro e login de usuários, autenticação básica.
- **Sprint 02:** Gestão de serviços.
- **Sprint 03:** Painel administrativo e validação de documentos.
- **Sprint 04:** Otimização de desempenho e testes finais.

---

### **9. Critérios de Aceitação**
- O sistema deve permitir o cadastro e login de usuários sem erros.
- O fluxo de solicitação e aceitação de serviços deve ser funcional.
- Documentos enviados devem ser validados corretamente pelo sistema.

---

### **10. Orçamento e Recursos**
- **Equipe:** 5 desenvolvedores.
- **Tempo estimado:** 3 meses.
- **Orçamento:** R$ 0,00 (projeto sem custos diretos, utilizando ferramentas gratuitas e/ou de código aberto sempre que possível).
<!-- - **Ferramentas:** Servidor em nuvem (AWS ou DigitalOcean), licenças de software necessárias. -->