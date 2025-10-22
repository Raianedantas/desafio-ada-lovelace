

## 1. Introdução

Este documento detalha os resultados da análise exploratória (Tarefa A2) realizada sobre o conjunto de dados brutos (`vendas (3).csv`). [cite_start]O objetivo é validar os problemas identificados no desafio[cite: 9], quantificar sua extensão e fornecer um direcionamento claro para a etapa de Transformação (T).

## 2. Visão Geral do Dataset

-   **Arquivo Analisado:** `vendas (3).csv`
-   **Dimensões:** 2000 linhas e 7 colunas.

### Estrutura e Tipos de Dados

| Coluna | Tipo (Dtype) | Valores Nulos | % Nulos |
| :--- | :--- | :--- | :--- |
| id_venda | `int64` | 0 | 0.00% |
| data_venda | `object` | 0 | 0.00% |
| cliente | `object` | 335 | 16.75% |
| produto | `object` | 2000 | 0.00% |
| quantidade | `object` | 0 | 0.00% |
| preco_unitario | `float64` | 0 | 0.00% |
| categoria | `object` | 52 | 2.60% |

---

## 3. Diagnóstico dos Problemas e Recomendações

[cite_start]A exploração confirma **todos** os problemas listados no desafio[cite: 9]. Abaixo está o detalhamento de cada um:

### [cite_start]Problema 1: Datas em Formatos Diferentes [cite: 10]

-   **Diagnóstico:** A coluna `data_venda` é do tipo `object` (texto) e não um formato `datetime`. A inspeção manual revela múltiplos formatos (ex: `AAAA/MM/DD`, `AAAA-MM-DD`, `DD-MM-AAAA`).
-   **Recomendação (Para Squad B):** Aplicar a função `pd.to_datetime()` para converter a coluna. [cite_start]Em seguida, padronizar para o formato `YYYY-MM-DD` conforme solicitado[cite: 28].

### [cite_start]Problema 2: Valores Ausentes (Cliente e Categoria) [cite: 10, 12]

-   **Diagnóstico:** Foram identificados valores nulos em duas colunas críticas:
    -   [cite_start]`cliente`: **335** linhas estão com cliente nulo[cite: 12].
    -   [cite_start]`categoria`: **52** linhas estão com categoria nula[cite: 10].
-   [cite_start]**Recomendação (Para Squad B):** Preencher todos os `NaN` em ambas as colunas com a string "Não informado", conforme a regra de negócio[cite: 29].

### [cite_start]Problema 3: Quantidade em Texto [cite: 10]

-   **Diagnóstico:** A coluna `quantidade` é do tipo `object` (texto). A análise revelou que, além de números, ela contém valores por extenso (ex: "três", "um", "cinco").
-   [cite_start]**Recomendação (Para Squad B):** Criar uma função de mapeamento (dicionário) para converter esses valores (ex: `{'três': 3, ...}`) e garantir que a coluna final seja do tipo `int`[cite: 30].

### [cite_start]Problema 4: Preços Negativos [cite: 11]

-   **Diagnóstico:** A coluna `preco_unitario` é `float64`, mas a filtragem (`df[df['preco_unitario'] < 0]`) revelou a existência de registros com preços negativos.
-   [cite_start]**Recomendação (Para Squad B):** Corrigir esses valores[cite: 31]. Sugerimos aplicar a função `abs()` na coluna para torná-los positivos, assumindo ser um erro de digitação.

## 4. Conclusão

A exploração está concluída. Os dados brutos foram extraídos com sucesso pela função `extract()` e todos os problemas de qualidade foram quantificados.

git config --global user.name "CAROLINA"
git config --global user.email "unhaca@gmail.com"
