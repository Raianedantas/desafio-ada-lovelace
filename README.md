# Projeto - Data Wrangling & Pipeline em Python

## Etapa A - Exploração & Extração

###  Descrição
Exploração e extração de dados brutos do CSV de vendas para preparação do pipeline ETL.

Este é um desafio da equipe SQUAD ADA LOVELACE  referente ao Bootcamp Business Intelligence 2025 Desafio Data Wrangling e Pipelines em Python  o qual o objetivo é a implementação de um pipeline de ETL (Extração, Transformação e Carga) 
para limpar e processar dados de vendas de uma startupNesta etapa, o foco é compreender o dataset, identificar inconsistências e preparar a função `extract()` para ser usada nas próximas fases (Transformação e Carga). 

---

### Estrutura do Projeto
- `exploracao.py` = exploracao.py: Script dedicado à Análise Exploratória de Dados (EDA). É usado para carregar, investigar, fatiar e filtrar os dados brutos para entender a fundo os problemas de qualidade.

- `pipeline.py` = O orquestrador principal do pipeline ETL. Este script contém a estrutura do processo (E-T-L) e a implementação da função extract(), responsável por carregar os dados brutos com logs de execução.

- `README.md` = O 'manual de instruções' principal do projeto (este próprio arquivo!). Ele explica o objetivo, lista os entregáveis de cada Squad e, o mais importante, ensina como instalar as dependências (requirements.txt) e rodar os scripts.

- `report_exploracao.md` = O relatório de análise (entregável da exploracao.py). Este documento resume as descobertas da exploração, quantifica problemas (nulos, formatos de data, texto em quantidade, etc.) e serve como o principal guia para o Squad B iniciar as transformações.

- `requirements.txt` = bibliotecas necessárias para rodar o projeto Estrutura do Projeto

---

###  Execução Local (Terminal ou VS Code)

```bash
pip install -r requirements.txt
python exploracao.py
```

##  Como Rodar o Projeto

Siga estas etapas para configurar o ambiente e executar os scripts.

1.  **Clone o Repositório**
    Baixe os arquivos do projeto para sua máquina local.

2.  **Crie um Ambiente Virtual**
    No terminal, dentro da pasta do projeto, crie um ambiente isolado:

    ```bash
    python -m venv venv
    ```

3.  **Ative o Ambiente Virtual**

      * No Windows:
        ```bash
        .\venv\Scripts\activate
        ```
      * No macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4.  **Instale as Dependências**
    Instale todas as bibliotecas necessárias que estão listadas no `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

5.  **Execute a Análise Exploratória (Squad A)**
    Para rodar o script de exploração e ver a análise dos dados brutos:

    ```bash
    python exploracao.py
    ```

6.  **Execute o Pipeline Principal**
    Para rodar o pipeline de ETL completo (Extração, Transformação e Carga):

    ```bash
    python pipeline.py
    ```

##### 🚀 Nossa Equipe e Divisão de Tarefas

Para organizar nosso fluxo de trabalho, dividimos o projeto em três Squads com focos de atuação distintos, baseados na ata de alinhamento do projeto. Cada squad teve autonomia para desenvolver suas soluções.

---

> ### 👩‍💻 SQUAD A – Exploração & Extração
>
> **Foco:** Preparar o ambiente, analisar os dados brutos, identificar problemas e construir a primeira etapa (`Extract`) do pipeline.
>
> **Membros:**
> * [RAINE DANTAS](https://github.com/Raianedantas)
> * [CAROLINA FREIRE](https://github.com/carolfsfreire)
>
> **Atribuições:**
> * **A1 (Fácil):** Configuração do ambiente, repositório, `README` inicial e `requirements.txt`.
> * **A2 (Fácil → Médio):** Análise exploratória de dados (EDA), filtros e ordenação.
> * **A3 (Médio):** Criação da função `extract()` com logs e da estrutura base do pipeline.
>
> **Entregáveis:**
> * `exploracao.py`
> * `report_exploracao.md`
> * `pipeline.py` (com a função `extract()`)

---

> ### 🛠️ SQUAD B – Transformações
>
> **Foco:** Limpar, tratar e enriquecer os dados. Esta é a etapa (`Transform`) onde a "mágica" da limpeza acontece.
>
> **Membros:**
> * [GABRIELLY LIMA](https://github.com/gabrielly-slima/gabrielly-slima)
> * [ALINE NASCIMENTO](https://github.com/alinelimx)
> * [HELENA NOCERA]()
>
> **Atribuições:**
> * **B1 (Médio):** Funções para padronizar datas (`padroniza_data`) e preencher valores nulos (`preenche_nulos`).
> * **B2 (Médio):** Tratamento de preços negativos, criação da coluna `valor_total` e política de log de dados descartados.
> * **B3 (Difícil):** Conversão da coluna `quantidade` (texto para int) e criação de testes unitários.
>
> **Entregáveis:**
> * `transform.py`
> * `tests/test_transform.py`

---

> ### 🗃️ SQUAD C – Carga, Modelo & Qualidade
>
> **Foco:** Carregar os dados limpos no banco de dados (`Load`), modelar as tabelas e garantir a qualidade final dos dados.
>
> **Membros:**
> * [CAMILE SANTANA](https://github.com/ichcamile)
> * [SOPHIA PERAZA](https://github.com/sopbit)
> * [ANA CLARA RODRIGUES](https://github.com/DevAnaClara)
>
> **Atribuições:**
> * **C1 (Médio):** Função `load(df)` para salvar os dados na tabela principal `tb_vendas`.
> * **C2 (Difícil):** Normalização da `tb_clientes`, criação de Chave Estrangeira (FK) e definição da ordem de carga.
> * **C3 (Difícil):** Implementação de validações (ex: Pandera), logging avançado e script SQL para consulta (`total_por_categoria.sql`).
>
> **Entregáveis:**
> * `load.py`
> * `schema.sql`
> * `consultas/total_por_categoria.sql`
