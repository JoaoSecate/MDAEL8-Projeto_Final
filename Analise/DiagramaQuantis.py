import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    # Faz a leitura do arquivo
    input_file = 'Datasets/glass_Normalized.data' #?
    names = ['RI','Na','Mg','Al','Si','K','Ca','Ba','Fe','Tipo']
    df = pd.read_csv(input_file,    # Nome do arquivo com dados
                      names = names) # Nome das colunas         

    atr = df['Na']
    print(atr.describe())
    fig = plt.boxplot(atr)
    plt.show()

if __name__ == "__main__":
    main()