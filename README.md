# 🌱 ECOFUTURO ESUDA

## Sobre o Projeto

O **ECOFUTURO ESUDA** é uma aplicação web de sustentabilidade que incentiva o uso de transportes ecológicos, recompensando os usuários com **moedas virtuais** que podem ser trocadas por benefícios reais oferecidos por parceiros da Faculdade ESUDA.

A proposta é transformar práticas sustentáveis do dia a dia — como andar de bicicleta, caminhar ou usar transporte público — em recompensas tangíveis, criando um ciclo de engajamento ambiental positivo.

---

## Arquitetura e Padrões de Projeto

O projeto foi evoluído para uma arquitetura Client-Server, dividida em duas camadas: um Front-end (interface do usuário) e um Back-end (API de regras de negócio).

**🔹 Back-end (Python/FastAPI)**

O back-end foi desenvolvido em Python 3.12 com o framework FastAPI, representando um motor de regras de negócio robusto. Ele está 100% funcional e totalmente integrado ao banco de dados Supabase. Atualmente, ele opera de forma independente do site, mas está pronto para ser consumido por qualquer aplicação cliente.

- **Banco de Dados:** Supabase (PostgreSQL).
- **Segurança:** Autenticação via JWT e criptografia de senhas com Bcrypt.
- **Documentação:** Swagger UI (OpenAPI) gerado automaticamente.
- **Validação:** Pydantic.
- **Requisitos:** 72 requisitos implementados (36 RF, 14 RN, 22 RNF).

**🔹 Front-end (JavaScript)**

A interface visual já está finalizada e hospedada na nuvem (Netlify), comunicando-se diretamente com o Supabase. A aplicação utiliza 4 padrões de projeto (GoF) na sua estrutura:

**Status de Integração**

O site e a API Python ainda não estão interligados diretamente, mas o Back-end está pronto para ser consumido por qualquer aplicação cliente.

### 🔹 Singleton — `SistemaEcofuturo`

O **Singleton** garante que exista apenas **uma única instância** da classe `SistemaEcofuturo` durante toda a execução da aplicação. Toda a lógica de negócio, estado dos usuários e regras de pontuação são gerenciados por essa instância única.

- Conecta-se ao **Supabase** (PostgreSQL) para persistência de dados
- Contém métodos para autenticação, registro de atividades, gerenciamento de vouchers, transferências, missões, ranking, medalhas, notificações e administração
- Utiliza consultas assíncronas (`async/await`) com o cliente Supabase JS

### 🔹 Facade — `EcofuturoFacade`

A **Facade** fornece uma interface simplificada entre a camada de UI (`app.js`) e o Singleton (`SistemaEcofuturo`). A camada de apresentação **nunca** acessa o Singleton diretamente — sempre passa pela Facade.

- Todos os métodos são `static`, facilitando o uso direto sem instanciação
- Delega cada chamada ao Singleton via `SistemaEcofuturo.getInstance()`
- Centraliza o ponto de acesso, tornando a manutenção mais simples

### 🔹 Strategy — `strategies/`

O **Strategy** encapsula diferentes algoritmos de cálculo de moedas e CO₂ em classes separadas, eliminando `switch`/`if` na lógica de negócio:

| Classe | Moedas/km | kg CO₂/km |
|---|---|---|
| `BicicletaStrategy` | 0.5 | 0.20 |
| `CaminhadaStrategy` | 0.4 | 0.15 |
| `TransportePublicoStrategy` | 0.3 | 0.10 |
| `CarroEletricoStrategy` | 0.2 | 0.05 |

### 🔹 Observer — `observers/`

O **Observer** desacopla as notificações visuais da lógica de negócio. Quando moedas são ganhas, resgates feitos ou vouchers expiram, o sistema dispara eventos para todos os observers registrados:

- `ToastObserver` — Exibe notificações toast no canto inferior direito
- `CoinAnimationObserver` — Mostra animação flutuante de moedas ganhas

### Fluxo de Dados

```
┌──────────┐      ┌──────────────────┐      ┌────────────────────┐      ┌──────────┐
│  app.js  │ ───▶ │ EcofuturoFacade  │ ───▶ │ SistemaEcofuturo   │ ───▶ │ Supabase │
│   (UI)   │      │   (Interface)    │      │   (Singleton)      │      │   (DB)   │
└──────────┘      └──────────────────┘      └────────────────────┘      └──────────┘
                                                       │
                                               ┌───────┴───────┐
                                               ▼               ▼
                                         strategies/      observers/
                                         (Strategy)       (Observer)
```

---

## 📂 Estrutura de Arquivos
```
ecofuturo/
├── backend/                    → API em Python/FastAPI (Hospedada no Render)
│   ├── app/                    → Routers, schemas e regras de negócio
│   └── requirements.txt        → Dependências do Python
├── index.html                  → SPA base (auth modal, headers, containers)
├── styles.css                  → Estilos globais (glassmorphism)
├── SistemaEcofuturo.js         → Singleton — lógica de negócio + queries Supabase
├── EcofuturoFacade.js          → Facade — interface simplificada para a UI
├── app.js                      → Camada de UI — SPA com loadPage(), event delegation
├── supabase-config.js          → Configuração do cliente Supabase (Front-end)
├── package.json                → Dependências do Front-end (Vitest, jsdom)
├── vitest.config.js            → Configuração do Vitest
├── strategies/                 → Strategy Pattern (cálculo de moedas/CO₂)
├── observers/                  → Observer Pattern (notificações visuais)
├── pages/                      → Páginas carregadas dinamicamente via fetch()
├── tests/                      → 173 testes unitários (Vitest + jsdom)
└── README.md                   → Este arquivo
---
```

## Tecnologias Utilizadas

- **HTML5** — Estrutura da página (SPA com páginas carregadas via fetch)
- **TailwindCSS (CDN)** — Estilização utilitária
- **CSS customizado (styles.css)** — Animações, glassmorphism e estilos complementares
- **JavaScript (ES Modules)** — Singleton + Facade + Strategy + Observer + SPA com event delegation
- **Supabase** — Banco de dados PostgreSQL + Autenticação (email/senha, confirmação desativada)
- **Chart.js** — Gráficos de relatórios
- **Google Fonts (Inter)** — Tipografia
- **Vitest + jsdom** — Testes unitários

---

## Funcionalidades

### 👤 Para Usuários Comuns

| Funcionalidade | Descrição |
|---|---|
| **Cadastro e Login** | Criação de conta com nome, e-mail, senha e tipo (aluno, professor, funcionário, comunidade externa) |
| **Registro de Atividades** | Registro de deslocamentos sustentáveis com tipo de transporte, distância, duração e data |
| **Ganho de Moedas** | Moedas calculadas automaticamente com base no transporte e distância |
| **Catálogo de Benefícios** | Visualização e reserva de recompensas (EcoBag, café, ingressos, descontos, etc.) |
| **Vouchers** | Ciclo completo: reservar → usar → cancelar, com geração de QR Code |
| **Relatórios Pessoais** | CO₂ reduzido e total de atividades, com filtro por período |
| **Relatórios da Comunidade** | Impacto coletivo com gráficos (Chart.js) |
| **Transferir Moedas** | Envio de moedas entre usuários |
| **Ranking** | Ranqueamento de usuários por moedas acumuladas |
| **Missões Diárias e Semanais** | Missões com barra de progresso e recompensas em moedas |
| **Medalhas** | 12 achievements por marcos (km, atividades, CO₂, posição no ranking) |
| **Desafios Mensais** | 5 desafios por tipo de transporte |
| **Notificações** | Central de notificações do sistema |
| **Mensagens** | Caixa de entrada com mensagens de outros usuários |

### 🛡️ Para Administradores

| Funcionalidade | Descrição |
|---|---|
| **Gerenciar Usuários** | Adicionar, editar, excluir usuários |
| **Gerenciar Parceiros** | Adicionar e remover empresas parceiras |
| **Gerenciar Benefícios** | Adicionar, excluir benefícios e atualizar estoques |
| **Relatório de Resgates** | Visão geral de todos os resgates realizados |

### ⏰ Expiração de Moedas

Moedas não utilizadas por **12 meses consecutivos** são automaticamente expiradas durante o login, com notificação ao usuário.

---

## Sistema de Moedas

As moedas são ganhas por quilômetro percorrido usando transportes sustentáveis:

| Transporte | Moedas/km |
|---|---|
| 🚲 Bicicleta | 0.5 |
| 🚶 Caminhada | 0.4 |
| 🚌 Transporte Público | 0.3 |
| ⚡ Carro Elétrico | 0.2 |

## Cálculo de CO₂ Reduzido

O impacto ambiental é calculado com base nos seguintes fatores de redução por km:

| Transporte | kg CO₂/km |
|---|---|
| 🚲 Bicicleta | 0.20 |
| 🚶 Caminhada | 0.15 |
| 🚌 Transporte Público | 0.10 |
| ⚡ Carro Elétrico | 0.05 |

---

## Credenciais de Acesso

### Administrador
- **E-mail:** `admin@ecofuturo.com`
- **Senha:** `admin123`

### Usuários comuns
Novos usuários podem ser criados pela tela de cadastro ou pelo painel administrativo.

---

## 🌐 Deploy e Nuvem

A arquitetura do projeto foi pensada para a nuvem, garantindo alta disponibilidade, segurança e escalabilidade.

**Acesse a aplicação online:** [ecofuturoesuda.netlify.app](https://ecofuturoesuda.netlify.app/)

### 🚀 Netlify (PaaS - Hospedagem do Front-end)

O front-end (site) está hospedado no **Netlify**, uma das plataformas mais modernas do mercado para aplicações web. A escolha do Netlify traz benefícios essenciais para o projeto:

- **CI/CD Automatizado (Integração e Entrega Contínuas):** O Netlify está conectado diretamente ao repositório do GitHub. Toda vez que uma nova atualização de código é enviada (via *push*), a plataforma detecta, compila e publica a nova versão do site automaticamente em poucos segundos, sem a necessidade de deploys manuais.
- **CDN Global:** Os arquivos do site são distribuídos em servidores (Edge Network) espalhados pelo mundo. Isso significa que, independentemente de onde o usuário esteja, o site carregará de forma extremamente rápida, a partir do servidor mais próximo.
- **HTTPS Seguro:** A plataforma gerencia e renova automaticamente os certificados de segurança (SSL), garantindo que o site seja sempre acessado via conexão criptografada (`https://`).
- **Rollbacks Fáceis:** Caso uma atualização apresente erro, é possível reverter o site para uma versão anterior com apenas um clique.

### 🗄️ Supabase (BaaS - Banco de Dados)

O **Supabase** atua como nosso *Backend as a Service*. Ele fornece toda a infraestrutura de banco de dados PostgreSQL na nuvem, além do sistema de autenticação. Ele conta com backups automáticos e garante que os dados dos usuários, atividades e vouchers estejam sempre seguros e disponíveis.

🚀 Render (PaaS - Hospedagem do Back-end)
O back-end (API em Python/FastAPI) está oficialmente hospedado e rodando no Render. A plataforma garante a execução contínua das regras de negócio e a segurança da aplicação, trazendo os seguintes benefícios:

* **CI/CD Automatizado:** O Render está integrado diretamente ao GitHub. A cada novo `push` na branch `main`, ele reconstrói a aplicação, instala as dependências (`requirements.txt`) e atualiza a API automaticamente, sem deploys manuais.
* **Variáveis de Ambiente Seguras:** Credenciais sensíveis (como as chaves do Supabase e o `SECRET_KEY`) não ficam expostas no código. Elas são configuradas de forma segura no painel do Render.
* **Documentação Pública (Swagger UI):** A API expõe automaticamente a documentação OpenAPI, permitindo que qualquer aplicação cliente teste as rotas publicamente.
* **Link da API:** [https://ecofuturo-esuda-cloud-ir.onrender.com/docs](https://ecofuturo-esuda-cloud-ir.onrender.com/docs)
* **Plano Free (Hibernação):** Para otimizar custos, o Render "hiberna" a API após 15 minutos de inatividade. A primeira requisição após esse período pode demorar cerca de 50 segundos para "acordar" o servidor (Cold Start), mas depois opera normalmente.


---

## Como Executar (Local)

**Importante:** O sistema usa `type="module"` no JavaScript, que **não funciona** abrindo o arquivo diretamente (`file://`). É necessário um servidor HTTP.

1. **Com Node.js (recomendado):**
   ```bash
   node server.js
   ```
   O servidor escuta na porta `8080` e serve `index.html` como padrão, com proteção contra path traversal.

2. **Com npx:**
   ```bash
   npx http-server -p 8080
   ```

3. **Com VS Code:** Instalar a extensão "Live Server" e clicar "Go Live"

4. **Com Python:**
   ```bash
   python -m http.server 8080
   ```

5. Abrir no navegador: `http://localhost:8080`

---

## Executar Testes

```bash
# Rodar todos os testes
npm test

# Modo watch (desenvolvimento)
npm run test:watch

# Com cobertura
npm run test:coverage
```

---

## Banco de Dados (Supabase)

O projeto utiliza o **Supabase** como infraestrutura de banco de dados e autenticação (BaaS):

- **Autenticação:** Supabase Auth (email/senha, confirmação de email desativada)
- **Banco:** PostgreSQL com tabelas: `usuario`, `parceiro`, `beneficio`, `atividade`, `emissao_co2`, `conversao_moedas`, `moeda`, `resgate`, `voucher`, `notificacao`, `mensagem`
- **RLS:** Liberado para todas as operações (anon key)
- **Trigger:** `on_resgate_insert` cria voucher + movimentação SAIDA na tabela `moeda`

**Conexão Atual:** O Front-end (site) conecta-se diretamente ao banco via `supabase-config.js` usando a anon key do projeto. A API em Python (Back-end) também possui sua própria integração segura com este mesmo banco de dados.

---

## Padrões Implementados (GoF)

| Padrão | Localização | Propósito |
|---|---|---|
| **Singleton** | `SistemaEcofuturo.js` | Instância única de lógica de negócio |
| **Facade** | `EcofuturoFacade.js` | Interface simplificada entre UI e lógica |
| **Strategy** | `strategies/` (5 classes) | Cálculo variável de moedas/CO₂ por transporte |
| **Observer** | `observers/` (3 classes) | Notificações visuais desacopladas |

## Testes

**173 testes unitários** distribuídos em 5 suites:

| Suite | Testes | O que cobre |
|---|---|---|
| `strategies.test.js` | 24 | 4 estratégias × 6 cenários (valores, zeros, negativos, etc.) |
| `observers.test.js` | 14 | ToastObserver, CoinAnimationObserver, interface Observer |
| `SistemaEcofuturo.test.js` | 119 | Singleton, login, cadastro, observer, atividades, benefícios, parceiros, vouchers, transferências, ranking, missões, medalhas, notificações, mensagens, expiração, CRUD |
| `EcofuturoFacade.test.js` | 10 | Delegação correta de todos os métodos da Facade |
| `smoke.test.js` | 6 | Importação sem erro de todos os módulos |

---

## Autores

**Igor Philipo Silva /  kamylle da Silva Alves de Almeida / Roseli Maria do Nascimento — Faculdade ESUDA
