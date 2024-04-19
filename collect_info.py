import pandas as pd
import re
import os

def extract_address_info(address):
    """ Extracts detailed information from the provided address. """
    parts = address.split(' - ')
    if len(parts) < 4:
        return [None] * 5

    endereco = parts[0].strip()
    bairro = parts[1].strip()
    municipio_uf_cep = parts[2].strip()

    cep_search = re.search(r'\d{5}-?\d{3}', parts[3])
    cep = cep_search.group(0) if cep_search else None

    municipio_uf = municipio_uf_cep.split('/')
    municipio = municipio_uf[0].strip() if municipio_uf else None
    uf = municipio_uf[1].strip() if len(municipio_uf) > 1 else None

    return [endereco, bairro, municipio, uf, cep]

def process_files(input_directory, output_directory):
    for filename in os.listdir(input_directory):
        file_path = os.path.join(input_directory, filename)
        if file_path.endswith('.csv') or file_path.endswith('.xlsx'):
            if file_path.endswith('.csv'):
                df = pd.read_csv(file_path, encoding='utf-8')
            elif file_path.endswith('.xlsx'):
                df = pd.read_excel(file_path)

            address_info = df['ENDERECO'].apply(extract_address_info)
            address_df = pd.DataFrame(address_info.tolist(), columns=['ENDERECO', 'BAIRRO', 'MUNICIPIO', 'UF', 'CEP'])

            df.drop(columns=['ENDERECO'], inplace=True)
            df_final = pd.concat([df, address_df], axis=1)

            # Save to CSV and XLSX in separate folders
            csv_output_path = os.path.join(output_directory, 'csvs', f'{filename[:-5]}.csv')
            xlsx_output_path = os.path.join(output_directory, 'xlsx', f'{filename[:-5]}.xlsx')

            os.makedirs(os.path.dirname(csv_output_path), exist_ok=True)
            os.makedirs(os.path.dirname(xlsx_output_path), exist_ok=True)

            df_final.to_csv(csv_output_path, index=False)
            df_final.to_excel(xlsx_output_path, index=False)
            print(f"Arquivos salvos em: {csv_output_path} e {xlsx_output_path}")

input_directory = './input'
output_directory = './output'

process_files(input_directory, output_directory)
