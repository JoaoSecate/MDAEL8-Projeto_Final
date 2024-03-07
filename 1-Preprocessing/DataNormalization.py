import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler


def main():
    # Faz a leitura do arquivo
    input_file = '0-Datasets/glass_Clear.data'
    output_file = '0-Datasets/glass_Normalized.data'
    names = ['RI','Na','Mg','Al','Si','K','Ca','Ba','Fe','Tipo'] 
    features = ['RI','Na','Mg','Al','Si','K','Ca','Ba','Fe']
    target = 'Tipo'
    df = pd.read_csv(input_file,    # Nome do arquivo com dados
                     names = names) # Nome das colunas                      
    ShowInformationDataFrame(df,"Dataframe original")

    df_original = df.copy()
    # Separating out the features
    x = df.loc[:, features].values
    
    # Separating out the target
    y = df.loc[:,[target]].values

    # Z-score normalization
    x_zcore = StandardScaler().fit_transform(x)
    normalized1Df = pd.DataFrame(data = x_zcore, columns = features)
    normalized1Df = pd.concat([normalized1Df, df[[target]]], axis = 1)
    ShowInformationDataFrame(normalized1Df,"Dataframe Z-Score Normalized")
    # Salva arquivo com normalização Z-Score
    normalized1Df.to_csv(output_file, header=False, index=False)  

    # Min-Max normalization
    x_minmax = MinMaxScaler().fit_transform(x)
    normalized2Df = pd.DataFrame(data = x_minmax, columns = features)
    normalized2Df = pd.concat([normalized2Df, df[[target]]], axis = 1)
    ShowInformationDataFrame(normalized2Df,"Dataframe Min-Max Normalized")
    # Salva arquivo com normalização Min-Max
    normalized2Df.to_csv(output_file, header=False, index=False)  


def ShowInformationDataFrame(df, message=""):
    print(message+"\n")
    print(df.info())
    print(df.describe())
    print(df.head(10))
    print("\n") 


if __name__ == "__main__":
    main()