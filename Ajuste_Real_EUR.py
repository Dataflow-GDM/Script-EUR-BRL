import pandas as pd
import os

# Caminho para a pasta com os arquivos CSV
folder_path = r'C:\Users\Mauro\Growth Digital Marketing\Joabe Onorato da Silva - Analise de Dados\CACTUS\Base'

# Listar todos os arquivos CSV na pasta
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        # Caminho completo do arquivo
        file_path = os.path.join(folder_path, filename)
        
        # Carregar o arquivo CSV, ignorando linhas problemáticas e definindo low_memory=False
        df = pd.read_csv(file_path, on_bad_lines='skip', low_memory=False)

        # Substituir o primeiro ponto (.) por vírgula (,) nas colunas em EUR
        for col in df.columns:
            if 'EUR' in col:
                df[col] = df[col].astype(str).str.replace('.', ',', 1)

        # Formatar colunas em BRL para o formato 00,00
        for col in df.columns:
            if 'BRL' in col:
                df[col] = df[col].apply(lambda x: f'R$ {float(x):,.2f}'.replace('.', ','))

        # Definir o caminho de saída para o arquivo ajustado
        output_path = os.path.join(folder_path, f"{os.path.splitext(filename)[0]}.csv")
        
        # Salvar o DataFrame ajustado em um novo arquivo CSV
        df.to_csv(output_path, index=False, sep=';')
        print(f"Arquivo ajustado salvo em: {output_path}")
