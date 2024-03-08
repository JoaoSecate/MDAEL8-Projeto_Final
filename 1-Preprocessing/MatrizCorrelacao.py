import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    # Faz a leitura do arquivo
    input_file = '0-Datasets/glass_Clear.data'
    names = ['RI','Na','Mg','Al','Si','K','Ca','Ba','Fe'] 
    df = pd.read_csv(input_file,    # Nome do arquivo com dados
                      names = names) # Nome das colunas                      

    correlacao = df.corr()
    sns.heatmap(correlacao, annot=True, fmt=".2f", cmap="coolwarm", cbar=True, square=True, linewidths=0.5)
    
    plt.title("Matriz de Correlação")
    plt.show()

if __name__ == "__main__":
    main()