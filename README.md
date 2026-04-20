# 🤖 Assistente Financeiro Inteligente com IA Generativa

## Contexto

Os assistentes virtuais no setor financeiro estão evoluindo de simples chatbots reativos para **agentes inteligentes e proativos**.

Neste projeto, foi desenvolvido um agente financeiro com IA Generativa com foco em:

* Ajudar usuários a entender opções de produtos financeiros
* Personalizar sugestões com base no perfil do usuário
* Atuar de forma educativa, sem realizar recomendações diretas
* Garantir segurança e evitar respostas imprecisas

A solução foi construída utilizando Python, Streamlit e integração com modelos de linguagem (LLM).

---

## O Que Foi Desenvolvido

### 1. Documentação do Agente

O agente foi projetado para atuar como um **assistente financeiro educativo**, com foco em:

* Identificação do perfil do usuário (conservador, moderado ou arrojado)
* Apoio na tomada de decisão financeira
* Comunicação clara e acessível

📄 Arquivo: `docs/01-documentacao-agente.md`

---

### 2. Base de Conhecimento

Foram utilizados dados mockados para simular o comportamento do agente:

| Arquivo                     | Formato | Utilização                       |
| --------------------------- | ------- | -------------------------------- |
| `perfil_investidor.json`    | JSON    | Definição de perfil do usuário   |
| `produtos_financeiros.json` | JSON    | Produtos financeiros disponíveis |

Os dados são utilizados para contextualizar as respostas da IA.

📄 Arquivo: `docs/02-base-conhecimento.md`

---

### 3. Prompts do Agente

Foi desenvolvido um conjunto de prompts com regras claras para garantir:

* Respostas educativas
* Ausência de recomendações diretas
* Linguagem simples
* Segurança contra alucinações

📄 Arquivo: `docs/03-prompts.md`

---

### 4. Aplicação Funcional

Foi desenvolvido um chatbot interativo com:

* Interface moderna em Streamlit
* Chat com efeito de digitação
* Feedback visual ("Pensando...")
* Integração com OpenAI

Além disso, o sistema conta com:

* Histórico persistente de conversas
* Títulos automáticos gerados por IA
* Resumo automático das conversas
* Busca, edição, fixação e exclusão de histórico

📁 Pasta: `src/`

---

### 5. Avaliação e Métricas

O agente foi avaliado com base em:

* Assertividade das respostas
* Coerência com o perfil do usuário
* Segurança (não recomendação direta)
* Clareza e utilidade

📄 Arquivo: `docs/04-metricas.md`

---

### 6. Pitch

Foi desenvolvido um pitch de 3 minutos apresentando:

* Problema
* Solução
* Demonstração
* Diferencial

📄 Arquivo: `docs/05-pitch.md`

---

## Estrutura do Repositório

/data
├── perfil_investidor.json
└── produtos_financeiros.json

//docs
├── 01-documentacao-agente.md
├── 02-base-conhecimento.md
├── 03-prompts.md
├── 04-metricas.md
└── 05-pitch.md

logs
└── histórico de conversas

/src
└── app.py

.env
.gitignore
requirements.txt
README.md

---

## Tecnologias Utilizadas

* Python
* Streamlit
* OpenAI API (GPT)
* JSON
* Dotenv

---

## Como Executar

1. Clonar o repositório

git clone https://github.com/williamd89/dio-assistente-financeiro
cd https://github.com/williamd89/dio-assistente-financeiro

2. Instalar dependências

pip install -r requirements.txt

3. Configurar variável de ambiente

Criar arquivo `.env`:

OPENAI_API_KEY=sua_chave

4. Executar o projeto

streamlit run src/app.py

---

## Diferenciais do Projeto

* Uso responsável de IA no contexto financeiro
* Interface moderna e interativa
* Experiência semelhante a produtos reais (UX avançada)
* Persistência e gestão completa de histórico
* Organização inteligente das conversas

---

## Observação

Este projeto tem caráter educacional e não substitui um consultor financeiro profissional.
