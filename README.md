# Ajuste de Arquivos CSV com Formatação de Valores em EUR e BRL

Este script automatiza o processamento de arquivos CSV em uma pasta específica, aplicando ajustes em valores monetários para os formatos padrão de EUR e BRL. O resultado é salvo em novos arquivos CSV no mesmo local.

---

## Funcionalidades

- **Leitura de Arquivos CSV**:
  - Processa todos os arquivos CSV em uma pasta especificada.
  - Ignora linhas problemáticas ao carregar os arquivos.

- **Formatação de Valores Monetários**:
  - Substitui o primeiro ponto (`.`) por vírgula (`,`) em colunas contendo "EUR".
  - Formata colunas contendo "BRL" para o formato monetário brasileiro (`R$ 00,00`).

- **Exportação**:
  - Salva os arquivos ajustados com o mesmo nome no formato CSV, sobrescrevendo os originais.

---

## Requisitos

- Python 3.x
- Biblioteca `pandas`

### Instalação do `pandas`

Para instalar a biblioteca, execute:

pip install pandas

![image](https://github.com/user-attachments/assets/66249606-76ab-4c46-b8ed-96373464125f)
