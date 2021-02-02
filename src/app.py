import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def main():
    obitos_2019 = carrega_dados('Dados/obitos-2019.csv')
    obitos_2020 = carrega_dados('Dados/obitos-2020.csv')
    tipo_doenca = np.append(obitos_2020['tipo_doenca'].unique(),'TODAS')
    tipo_estado = np.append(obitos_2020['uf'].unique(),'BRASIL')

    
    st.title("Análise de Óbitos COVID-19")
    
    st.markdown('Este trabalho analisa os obitos de covid do ano de **2019 e 2020**')
    
    
    
    opcao_doenca = st.selectbox('Selecione o tipo da doença respiratoria:',tipo_doenca)
    opcao_estado = st.selectbox('Selecione o estado federativo:',tipo_estado)
    
    
    fig = grafico_comparativo(obitos_2019, obitos_2020, opcao_doenca, opcao_estado)

    st.pyplot(fig)
    
    st.text("Dados Brutos")
    
    
    
def carrega_dados(caminho):
    dados = pd.read_csv(caminho)
    return dados     




def grafico_comparativo(dados_2019, dados_2020, causa='TODAS',uf='BRASIL'):
    
    if uf == 'BRASIL':
        total_2019 = dados_2019.groupby('tipo_doenca').sum()
        total_2020 = dados_2020.groupby('tipo_doenca').sum()
        if causa =='TODAS':
            lista = int(total_2019['total'].sum()) , int(total_2020['total'].sum())
        else:
            lista = int(total_2019.loc[causa]) , int(total_2020.loc[causa])
    

    else:
        total_2019 = dados_2019.groupby(['uf','tipo_doenca']).sum()
        total_2020 = dados_2020.groupby(['uf','tipo_doenca']).sum()
        if causa =='TODAS':
            lista = int(total_2019.loc[uf].sum()) , int(total_2020.loc[uf].sum())
        else:    
            lista = int(total_2019.loc[uf ,causa]) , int(total_2020.loc[uf,causa])
        
        
    fig, ax = plt.subplots()
    dados = pd.DataFrame({'Total':lista,
                         'Ano':[2019,2020]})    
    ax = sns.barplot(x='Ano', y='Total',data=dados)
    
    

    ax.set_title('Obitor por '+causa+' em: '+uf)
    
    
    return fig 










              
if __name__ == "__main__":
    main()                                               