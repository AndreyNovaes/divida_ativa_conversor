import pandas as pd
import re

def extract_address_info(address):
    """ Extracts detailed information from the provided address. """
    parts = address.split(' - ')
    if len(parts) < 4:
        return [None, None, None, None, None]

    endereco = parts[0].strip()
    bairro = parts[1].strip()
    municipio_uf_cep = parts[2].strip()

    # Extract the CEP using regex
    cep_search = re.search(r'\d{5}-?\d{3}', parts[3])
    cep = cep_search.group(0) if cep_search else None

    # Split the municipio_uf part on '/' to separate the municipality and UF
    municipio_uf = municipio_uf_cep.split('/')
    municipio = municipio_uf[0].strip()
    uf = municipio_uf[1].strip() if len(municipio_uf) > 1 else None

    return [endereco, bairro, municipio, uf, cep]

def process_and_save_xlsx(input_file_path, output_file_path):
    # Verifica a extensão do arquivo de entrada para decidir como processar
    if input_file_path.endswith('.csv'):
        # Lê arquivo CSV usando pandas
        df = pd.read_csv(input_file_path, delimiter=',', names=['CODIGO', 'CPF', 'NOME', 'EMAIL', 'TELEFONE', 'ENDERECO', 'DATA DE NASCIMENTO', 'SEXO', 'ESTADO CIVIL'], header=0)
    elif input_file_path.endswith('.xlsx'):
        # Lê arquivo XLSX usando pandas
        df = pd.read_excel(input_file_path, names=['CODIGO', 'CPF', 'NOME', 'EMAIL', 'TELEFONE', 'ENDERECO', 'DATA DE NASCIMENTO', 'SEXO', 'ESTADO CIVIL'], header=0)
    else:
        # Se o arquivo não for nem CSV nem XLSX, lança um erro
        raise ValueError(f"Invalid file extension: {input_file_path}")

    # Aplica a função extract_address_info em cada endereço e converte o resultado em DataFrame
    address_info = df['ENDERECO'].apply(extract_address_info)
    address_df = pd.DataFrame(address_info.tolist(), columns=['ENDERECO', 'BAIRRO', 'MUNICIPIO', 'UF', 'CEP'])

    # Converte o índice do DataFrame de endereços em uma série
    address_df.index = address_df.index.to_series().groupby(address_df.index).first()

    # Verifica se os comprimentos dos índices são iguais
    if len(df.index) != len(address_df.index):
        raise ValueError("Os comprimentos dos índices dos DataFrames não são iguais.")

    # Remove a coluna 'ENDERECO' do DataFrame original
    df.drop(columns=['ENDERECO'], inplace=True)

    # Combina o DataFrame original com o novo DataFrame de endereços
    df_final = pd.concat([df, address_df], axis=1)

    # Seleciona as colunas de interesse para o arquivo final
    df_final = df_final[['CODIGO', 'CPF', 'NOME', 'ENDERECO', 'BAIRRO', 'MUNICIPIO', 'UF', 'CEP']]

    # Salva o DataFrame final em um arquivo XLSX no caminho especificado
    df_final.to_excel(output_file_path, index=False)
    print(f"Arquivo salvo em: {output_file_path}")

# Paths to the input and output CSV files
input_file_path = './input/RegistroDeDados.csv'
output_file_path = './output/RegistroDeDadosConvertido.xlsx'

# Execute the processing and saving function
process_and_save_xlsx(input_file_path, output_file_path)