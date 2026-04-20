# 💰 Assistente Financeiro com IA

## 📌 Sobre o Projeto

Este projeto consiste no desenvolvimento de um assistente financeiro inteligente, utilizando IA generativa, com o objetivo de ajudar usuários a entender opções de produtos financeiros de forma simples, segura e personalizada.

A solução foi construída com foco em experiência do usuário (UX), segurança e boas práticas no uso de inteligência artificial, evitando recomendações diretas e promovendo educação financeira.

---

## 🎯 Problema

Muitas pessoas têm dificuldade em escolher produtos financeiros por falta de conhecimento sobre conceitos como risco, liquidez e rentabilidade.

Isso pode levar à inércia (dinheiro parado) ou decisões inadequadas.

---

## 💡 Solução

Foi desenvolvido um agente conversacional que:

* Identifica o perfil do usuário (conservador, moderado ou arrojado)
* Considera fatores como objetivo, prazo e tolerância a risco
* Apresenta opções de produtos financeiros adequadas ao perfil
* Explica cada opção de forma clara e acessível
* NÃO realiza recomendações diretas (abordagem educativa)

---

## 🧠 Funcionalidades

### 💬 Chat Inteligente

* Interface conversacional moderna (Streamlit)
* Respostas com efeito de digitação
* Feedback visual de processamento ("Pensando...")

### 📊 Perfil do Usuário

* Coleta de:

  * Objetivo
  * Prazo
  * Tolerância a risco
  * Experiência
* Identificação automática do perfil

### 📜 Histórico de Conversas

* Persistência em arquivos JSON
* Recuperação automática ao reabrir o sistema
* Títulos gerados automaticamente por IA
* Resumo automático das conversas
* Busca por histórico

### ⚙️ Gestão de Conversas

* Fixar conversas importantes 📌
* Renomear conversas ✏️
* Deletar conversas 🗑️
* Criar nova conversa ➕

### 💡 Experiência do Usuário

* Perguntas rápidas (atalhos)
* Interface limpa e responsiva
* Navegação semelhante a aplicações reais de IA

---

## 🔐 Segurança e Boas Práticas

O agente foi projetado com foco em uso responsável de IA:

* Não realiza recomendações financeiras diretas
* Não promete retornos
* Atua apenas de forma educativa
* Solicita contexto antes de responder
* Evita alucinações com regras no prompt

---

## 🏗️ Arquitetura

Usuário → Interface (Streamlit) → LLM (OpenAI) → Base de Dados (JSON)

---

## 📁 Estrutura do Projeto

/data
├── perfil_investidor.json
└── produtos_financeiros.json

/docs
├── 01-documentacao-agente.md
├── 02-base-conhecimento.md
├── 03-prompts.md
├── 04-metricas.md
└── 05-pitch.md

/logs
└── histórico de conversas

/src
└── app.py

.env
.gitignore
README.md
requirements.txt

---

## ⚙️ Tecnologias Utilizadas

* Python
* Streamlit
* OpenAI API (GPT)
* JSON (persistência de dados)
* Dotenv

---

## 🚀 Como Executar

### 1. Clonar o repositório

git clone [<SEU_REPO>](https://github.com/williamd89/dio-assistente-financeiro.git)
cd [<SEU_REPO>](https://github.com/williamd89/dio-assistente-financeiro.git)

### 2. Instalar dependências

pip install -r requirements.txt

### 3. Configurar variável de ambiente

Criar arquivo `.env`:

OPENAI_API_KEY=sua_chave_aqui

### 4. Executar o projeto

streamlit run src/app.py

---

## 🎥 Demonstração

Adicione aqui o link do vídeo do pitch

---

## 📊 Diferenciais do Projeto

* Uso responsável de IA no contexto financeiro
* Experiência semelhante a produtos reais (UX avançada)
* Persistência e gestão completa de histórico
* Organização inteligente das conversas
* Interface moderna e interativa

---

## 📌 Observação

Este projeto tem caráter educacional e ndão substitui a orientação de um profissional financeiro.

---

## 👨‍💻 Autor

Projeto desenvolvido como parte de desafio prático da DIO.
