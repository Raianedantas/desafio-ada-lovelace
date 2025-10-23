import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract(file_path):
    """
    Função para extrair dados de um arquivo CSV.
    """
    logging.info(f"Iniciando a extração do arquivo: {file_path}")
    try:
        df = pd.read_csv(file_path)
        logging.info("Extração concluída com sucesso.")
        return df
    except FileNotFoundError:
        logging.error(f"Arquivo não encontrado no caminho: {file_path}")
        return None


if __name__ == "__main__":
    logging.info("Iniciando o pipeline de dados de vendas.")

    vendas_df = extract('data/vendas.csv')

    if vendas_df is not None:
        logging.info("Dados extraídos:")
        print(vendas_df.head())

    logging.info("Pipeline concluído.")