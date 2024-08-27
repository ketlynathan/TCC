import pandas as pd
from loguru import logger

def limpar_converter_dataframe(df):
    # Função para converter a data
    def converter_data(data):
        componentes = data.split(',')[1].strip().split('/')
        
        #logger.info("data no formato %m/%d/%Y")
            
        return pd.to_datetime(data.split(',')[1].strip(), format='%m/%d/%Y').strftime('%Y-%m-%d')

    # Aplicar a função converter_data à coluna 'Data'
    df['Date'] = df['Date'].apply(converter_data)
    

    # Limpeza da coluna 'Distancia'
    df['Distance'] = df['Distance'].str.replace('\n', '').str.replace(' km', '').str.replace(',', '.').str.strip()
    df['Distance'] = df['Distance'].str.extract(r'([\d\.]+)').astype(float)

    # Limpeza da coluna 'Elevacao'
    df['Elevation'] = df['Elevation'].str.replace('\n', '').str.replace(' m', '').str.strip()
    df['Elevation'] = df['Elevation'].str.extract(r'(\d+)').astype(int)

    # Limpeza da coluna 'Title'
    df['Type'] = df['Type'].str.strip()
    # Substituir os valores na coluna 'Tipo' conforme especificado
    df['Type'] = df['Type'].replace({'Pedalada': 'Ride', 'Caminhada': 'Walk', 'Corrida': 'Run'})

    df['Title'] = df['Title'].str.replace('\n', '')

    # Ajuste na coluna 'Tempo'
    df['Time'] = df['Time'].apply(lambda x: '00:' + x if isinstance(x, str) and len(x) == 5 else x)

    #caminho_arquivo = "./strava/view/sports.xlsx"

    # Salvar o DataFrame no arquivo Excel
    #df.to_excel(caminho_arquivo, index=False)

   # print(f"DataFrame salvo com sucesso em {caminho_arquivo}")
    
    return df

