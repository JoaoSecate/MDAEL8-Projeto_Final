import pandas as pd
import numpy as np

def main():
    # Faz a leitura do arquivo
    input_file = '0-Datasets/glass_Clear.data'
    names = ['RI','Na','Mg','Al','Si','K','Ca','Ba','Fe']
    df = pd.read_csv(input_file,    # Nome do arquivo com dados
                      names = names) # Nome das colunas         

    atributo = df['Na']
    print(atributo)
    print(atributo.describe())
    print(atributo.std())

if __name__ == "__main__":
    main()