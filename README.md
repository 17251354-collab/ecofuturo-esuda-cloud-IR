## 🌱 ECOFUTURO ESUDA

Sobre o Projeto
O ECOFUTURO ESUDA é uma aplicação web de sustentabilidade que incentiva o uso de transportes ecológicos, recompensando os usuários com moedas virtuais que podem ser trocadas por benefícios reais oferecidos por parceiros da Faculdade ESUDA.

A proposta é transformar práticas sustentáveis do dia a dia — como andar de bicicleta, caminhar ou usar transporte público — em recompensas tangíveis, criando um ciclo de engajamento ambiental positivo.

##Arquitetura do Back-end e Status do Sistema

O projeto possui uma arquitetura completa dividida em Front-end e Back-end:
- Back-end (Python/FastAPI): Foi desenvolvido um motor de regras de negócio robusto em Python. Ele está 100% funcional, documentado via Swagger e totalmente integrado ao banco de dados Supabase. Atualmente, ele opera de forma independente do site.
- Front-end (Site): A interface visual já está finalizada e hospedada na nuvem (Netlify), comunicando-se diretamente com o Supabase.
- Status de Integração: O site e a API Python ainda não estão interligados diretamente, mas o Back-end está pronto para ser consumido por qualquer aplicação cliente.

##Arquitetura e Padrões de Projeto
A aplicação utiliza 4 padrões de projeto (GoF) na sua estrutura:

🔹 Singleton — SistemaEcofuturo
O Singleton garante que exista apenas uma única instância da classe SistemaEcofuturo durante toda a execução da aplicação. Toda a lógica de negócio, estado dos usuários e regras de pontuação são gerenciados por essa instância única.
- Conecta-se ao Supabase (PostgreSQL) para persistência de dados
- Contém métodos para autenticação, registro de atividades, gerenciamento de vouchers, transferências, missões, ranking, medalhas, notificações e administração
- Utiliza consultas assíncronas (async/await) com o cliente Supabase JS

🔹 Facade — EcofuturoFacade
A Facade fornece uma interface simplificada entre a camada de UI (app.js) e o Singleton (SistemaEcofuturo). A camada de apresentação nunca acessa o Singleton diretamente — sempre passa pela Facade.
- Todos os métodos são static, facilitando o uso direto sem instanciação
- Delega cada chamada ao Singleton via SistemaEcofuturo.getInstance()
- Centraliza o ponto de acesso, tornando a manutenção mais simples

🔹 Strategy — strategies/
O Strategy encapsula diferentes algoritmos de cálculo de moedas e CO₂ em classes separadas, eliminando switch/if na lógica de negócio:
