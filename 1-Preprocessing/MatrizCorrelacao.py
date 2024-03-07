import pandas as pd 
import numpy as np
import statsmodels.api as sm #### biblioteca para plotar correlacao
import matplotlib.pyplot as plt

def main():
    # Faz a leitura do arquivo
    input_file = '0-Datasets/glass_Clear.data'
    output_file = '0-Datasets/glass_Normalized.data'
    names = ['RI','Na','Mg','Al','Si','K','Ca','Ba','Fe'] 
    features = ['RI','Na','Mg','Al','Si','K','Ca','Ba','Fe']
    df = pd.read_csv(input_file,    # Nome do arquivo com dados
                      names = names) # Nome das colunas                      
    #ShowInformationDataFrame(df,"Dataframe original")

    df_original = df.copy()
    # Separating out the features
    x = df.loc[:, features].values

    correlacao = df.corr()
    sm.graphics.plot_corr(correlacao, xnames=correlacao.columns)
    plt.title("Matriz de Correlação")
    plt.show()


if __name__ == "__main__":
    main()