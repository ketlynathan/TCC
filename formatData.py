import pandas as pd
from loguru import logger

def limpar_e_converter_dataframe(df):
    # Função para converter a data
    def converter_data(data):
        componentes = data.split(',')[1].strip().split('/')
        if len(componentes[0]) == 2:
            return pd.to_datetime(data.split(',')[1].strip(), format='%d/%m/%Y').strftime('%Y-%m-%d')
        else:
            return pd.to_datetime(data.split(',')[1].strip(), format='%m/%d/%Y').strftime('%Y-%m-%d')

    # Aplicar a função converter_data à coluna 'Data'
    df['Data'] = df['Data'].apply(converter_data)

    # Limpeza da coluna 'Distancia'
    df['Distancia'] = df['Distancia'].str.replace('\n', '').str.replace(' km', '').str.replace(',', '.').str.strip()
    df['Distancia'] = df['Distancia'].str.extract(r'([\d\.]+)').astype(float)

    # Limpeza da coluna 'Elevacao'
    df['Elevacao'] = df['Elevacao'].str.replace('\n', '').str.replace(' m', '').str.strip()
    df['Elevacao'] = df['Elevacao'].str.extract(r'(\d+)').astype(int)

    # Limpeza da coluna 'Title'
    df['Title'] = df['Title'].str.strip()
    # Substituir os valores na coluna 'Tipo' conforme especificado
    df['Tipo'] = df['Tipo'].replace({'Pedalada': 'Ride', 'Caminhada': 'Walk', 'Corrida': 'Run'})

    # Ajuste na coluna 'Tempo'
    df['Tempo'] = df['Tempo'].apply(lambda x: '00:' + x if isinstance(x, str) and len(x) == 5 else x)
    # Retornar o DataFrame limpo e convertido
    return df

