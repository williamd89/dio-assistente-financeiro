# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `perfil_investidor.json` | JSON | Classificar o perfil do usuário com base na tolerância a risco |
| `produtos_financeiros.json` | JSON | Sugerir produtos financeiros compatíveis com o perfil |

> [!TIP]
> Os dados utilizados são mockados e foram criados para fins educacionais.

---

## Adaptações nos Dados

Os dados foram criados manualmente com foco em simplicidade e clareza.

As principais adaptações foram:

- Definição de três perfis de investidor (conservador, moderado e arrojado)  
- Classificação dos produtos financeiros por nível de risco  
- Inclusão de descrições simples para facilitar a explicação ao usuário  

---

## Estratégia de Integração

### Como os dados são carregados?

Os arquivos JSON são carregados no início da execução da aplicação e armazenados em memória.

---

### Como os dados são usados no prompt?

Os dados são utilizados de forma indireta:

- O sistema identifica o perfil do usuário com base nas respostas  
- Os produtos são filtrados de acordo com o nível de risco  
- O modelo de linguagem utiliza essas informações para gerar respostas explicativas  

---

## Exemplo de Contexto Montado


> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:

Nome: Usuário
Objetivo: Investir com segurança
Prazo: Curto prazo
Tolerância a risco: Baixa
Experiência: Iniciante
Perfil identificado: Conservador

Produtos sugeridos:

Poupança: Alta liquidez e baixo risco
CDB: Retorno previsível e baixo risco
Tesouro Direto: Segurança e opções de prazo

Observação:
As sugestões são baseadas no perfil informado e têm caráter educativo.
```
